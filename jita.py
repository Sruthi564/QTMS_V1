import requests
import json
import time
from bson import json_util #pip install mongo
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.exceptions import ConnectionError, Timeout
#from base64 import decodestring as base64decode
import base64
from requests.auth import HTTPDigestAuth
from collections import OrderedDict
from functools import wraps


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
JITA_USER = base64.decodebytes(b'YWdhdmVfYm90')
JITA_PASSWORD = base64.decodebytes(b'YWRtaW4=')


def retry(exceptions, tries=4, delay=3, backoff=2, logger=None):
    """
    Retry calling the decorated function using an exponential backoff.

    Args:
        exceptions: The exception to check. may be a tuple of
            exceptions to check.
        tries: Number of times to try (not retry) before giving up.
        delay: Initial delay between retries in seconds.
        backoff: Backoff multiplier (e.g. value of 2 will double the delay
            each retry).
        logger: Logger to use. If None, print.
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except exceptions as e:
                    msg = '{}, Retrying in {} seconds...'.format(e, mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry


class Jita(object):
    """Class for performing Jita operations"""

    def __init__(self):
        self.jita_host = 'jita.eng.nutanix.com'
        self.jita_api = 'api/v2'
        self.session = Jita.establish_session()
        self.api_call_timeout = 300
        self.tasks_ids = []
        self.jps_not_triggered = []
        self.pc_url = u'http://endor.dyn.nutanix.com/builds/PC-builds/{}/{}/release/'

    def build_jita_url(self, url_param):
        jita_query = 'https:' + '//' + self.jita_host + '/' + self.jita_api + '/' + \
                     url_param
        return jita_query

    def get_job_profile_id(self, jp_name):
        r = self.get_jita_job_profile(jp_name)
        if r is not None:
            response = json.loads(r.content)
            for key in response["data"]:
                if '_id' in key:
                    jp_id = key['_id']['$oid']
                    print("Job Profile : {} ID is : {}".format(jp_name, jp_id))
                    return jp_id
                else:
                    print("No ID returned for Job Profile: {}".format(jp_name))
                    return None
        else:
            return None

    def get_jita_job_profile(self, jp_name):
        params ={
            "raw_query": json_util.dumps({
                "name": jp_name
        })
        }
        url = self.build_jita_url('job_profiles')
        try:
            r = requests.get(url=url, params=params, verify=False)
            if r.ok:
                return r
        except requests.RequestException as e:
            print("Bad Request for JP: {}, error : {}".format(jp_name, str(e)))
        return None

    def fetch_job_profile_payload(self, jp_id):
        url = self.build_jita_url('job_profiles') + '/' + jp_id
        if self.session is not None:
            r = self.session.get(url)
            if r.ok:
                response = json.loads(r.content)
                payload = response["data"]
                return payload
        return None

    def update_job_profile_payload(self, jp_id, jp_name, payload):
        #print "Payload ::: {}\n".format(payload)
        if jp_id is not None:
            #payload[u'emails'] = fqa_id
            url = self.build_jita_url('job_profiles')+'/'+jp_id
            if self.session is not None:
                r = self.session.put(url, json=payload, verify=False)
                if r.ok:
                    response = json.loads(r.content)
                    if response['success']:
                        print(response['message'] + ' with Name: {} and ID: {}'.format(jp_name, jp_id))
                    else:
                        print('Job profile: {} not updated with payload'.format(jp_name))
                else:
                    print('Job profile: {} not updated with payload'.format(jp_name))
            else:
                print('Session not established')
        else:
            print("Job Profile ID is: {} for JP: {}".format(jp_id, jp_name))

    @staticmethod
    def establish_session():
        try:
            print("Establishing Session")
            session = requests.Session()
            session.auth = (JITA_USER, JITA_PASSWORD)
            return session
        except Exception as e:
            print("Session Error: {}".format(str(e)))
        return None

    @retry((ConnectionError, Timeout))
    def trigger_job_profile(self, jp_name, jp_id, fqa_id, payload, category=None, sub_component=None):
        url = self.build_jita_url('job_profiles') + '/' + jp_id + '/' + 'trigger'
        if self.session is not None:
            r = self.session.post(url, json=payload, verify=False, timeout=self.api_call_timeout)
            if r.ok:
                response = json.loads(r.content)
                if response['success']:
                    print(response['message'] + ' : {}'.format(jp_name))
                    print("Task id for Job Profile: {} is : {}".format(jp_name, response['task_ids']))
                    task_dict = response['task_ids'][0]
                    task_dict['jp_name'] = jp_name
                    task_dict['fqa_id'] = fqa_id
                    task_dict['category'] = category
                    task_dict['sub-component'] = sub_component
                    task_dict['branch'] = payload['git']['branch']
                    self.tasks_ids.append([task_dict])
                else:
                    print("Job profile: {} not triggered".format(jp_name))
                    self.jps_not_triggered.append({jp_name: jp_id})
            else:
                print("Job profile: {} not triggered".format(jp_name))
                self.jps_not_triggered.append({jp_name: jp_id})
        else:
            print('Session not established')

    @staticmethod
    def fetch_status_task_id(task_id):
        status = ""
        if task_id:
            print("Fetching status of task: {}".format(task_id))
            url = "https://10.4.66.84/api/v2/agave_tasks/%s" % task_id
            try:
                print("fetch_status_task_id , url sent is: {}".format(url))
                r = requests.get(url, auth=HTTPDigestAuth(JITA_USER, JITA_PASSWORD),
                                 verify=False)
            except requests.RequestException as e:
                print("fetch_status_task_id, request exception observed: {}".format(str(e)))
                return status
            except Exception as e:
                print ("fetch_status_task_id, general exception caught is : {}".format(str(e)))
                return status

            if r.ok:
                r_data = json.loads(r.content)
                print("fetch_status_task_id, received a response...")
                if 'status' in r_data['data']:
                    #print "Data: {}".format(r_data['data'])
                    status = r_data['data']['status']
                    print("Task ID:{} has status : {}".format(task_id, status))
                    return status
            else:
                print("Request for fetching task i: {} status failed".format(task_id))
        else:
            print("fetch_status_task_id", "Param task id is mandatory")
        return status

    def get_smoke_passed_build(self):
        pass

    def get_jp_name_from_jita_task(self, task_id):
        if task_id:
            url = "https://10.4.66.84/api/v2/agave_tasks/%s" % task_id
            try:
                r = requests.get(url, auth=HTTPDigestAuth(JITA_USER, JITA_PASSWORD),
                                 verify=False)
            except requests.RequestException as e:
                print ("Request exception observed: {} while getting job profile name from task id".format(str(e)))
            except Exception as e:
                print ("Request exception observed: {} while getting job profile name from task id".format(str(e)))

            if r.ok:
                r_data = json.loads(r.content)
                print ("Getting job profile name from task id: {}".format(task_id))
                return r_data["data"]

    def clone_job_profile(self, payload1, payload2, clone_from_branch, clone_to_branch, sub_component, category, max_dep):
        if self.session is not None:
            payload1.update(payload2)
            jp_new_name = payload1['name'].replace(clone_from_branch, clone_to_branch)
            payload1['name'] = jp_new_name
            payload1['description'] = jp_new_name
            for tag in payload1['tester_tags']:
                if 'max_deployments' in tag:
                    payload1['tester_tags'].remove(tag)
                    payload1['tester_tags'].extend(max_dep)
            del payload1[u'_id']
            print ("Cloning JP: {}".format(payload1['name']))
            url = "https://jita.eng.nutanix.com/api/v2/job_profiles"
            r = self.session.post(url, json=payload1, verify=False, timeout=self.api_call_timeout)
            if r.ok:
                r_data = json.loads(r.content)
                if r_data['success']:
                    print ("JP: {} successfully cloned with JP ID: {}".format(payload1['name'],
                                                                             r_data['id']))
                    return OrderedDict({"JP_NAME": payload1['name'], "sub-component": sub_component, "category": category,
                                        "JP_ID": r_data['id'], "max_dep": max_dep})
            else:
                print ("Clone Request Failed for the JP: {}".format(payload1['name']))
                return None
        else:
            print ("Clone of JP: {} Failed".format(payload1['name']))
            return None

    def get_latest_smoke_passed_commit(self, branch):
        print("Getting smoke passed build for the branch : {}".format(branch))
        url = "http://jita/api/v1/commits/latest_smoke_passed?branch={}".format(branch)
        if self.session is not None:
            try:
                r = self.session.get(url)
            except Exception as e:
                print ("Failed to get smoke passed build: {}".format(str(e)))
                return None

            if r.ok:
                r_data = json.loads(r.content)
                if r_data['success']:
                    print ("Successfully got smoke passed build for branch: {}".format(branch))
                    return r_data['data']['commit_id']
        else:
            return None

    def get_jita_testset(self, test_set_name):
        params ={
            "raw_query": json_util.dumps({
                "name": test_set_name
        })
        }
        url = "https://jita.eng.nutanix.com/api/v2/agave_test_sets"
        if self.session is not None:
            try:
                r = self.session.get(url=url, params=params, verify=False)
            except Exception as e:
                print("Failed to get Test Set: {} details : {}".format(test_set_name, str(e)))
                return None
            if r.ok:
                r_data = json.loads(r.content)
                if r_data["success"]:
                    return r_data['data'][0][u'_id'][u'$oid']
        else:
            print("Failed to get Test Set Details")
            return None

    def create_compatilibility_job_profiles(self, component, sample_payload,
                                            payload, component_values, matrix, pc_build):
        if self.session is not None:
            payload['name'] = 'Compatibility_Acropolis_MTS_Nutest_' + component + "_" + \
                matrix["pe"] + "_" + matrix["pc"]
            payload['description'] = payload['name']
            payload['emails'] = component_values[component][0]['email']
            payload['nutest_branch'] = component_values[component][0]['nutest_branch']
            payload['git'] = {
                u'repo': u'main',
                u'branch': component_values[component][0]['nos_branch']
            }
            payload['cluster_selection'] = {
                u'pool_name': component_values[component][0]['pool_name'],
                u'by_node_pool': True
            }
            test_set_id = self.get_jita_testset(component_values[component][0]['test_set'])
            if test_set_id is not None:
                payload['test_sets'] = [{
                    u'$oid': test_set_id}]
            else:
                payload['test_sets'] = [{
                    u'$oid': ''}]
            if pc_build[0]["commit_id"] is not None:
                pc_url = self.pc_url.format(pc_build[0]["branch"], pc_build[0]["commit_id"])
            else:
                pc_commit = self.get_latest_smoke_passed_commit(pc_build[0]["branch"])
                if pc_commit is not None:
                    pc_url = self.pc_url.format(pc_build[0]["branch"], pc_commit)
                else:
                    pc_url = self.pc_url.format(pc_build[0]["branch"], 'latest')
            payload['resource_manager_json'] = dict(PRISM_CENTRAL={
                u'build': {
                    u'nos_build_url': pc_url
            }
            })
            sample_payload.update(payload)
            if '_id' in sample_payload:
                del sample_payload[u'_id']
            print("Creating JP: {}".format(sample_payload['name']))
            url = "https://jita.eng.nutanix.com/api/v2/job_profiles"
            print("Payload: {}".format(sample_payload))
            r = self.session.post(url, json=sample_payload, verify=False, timeout=self.api_call_timeout)
            if r.ok:
                r_data = json.loads(r.content)
                if r_data['success']:
                    print("JP: {} successfully created with JP ID: {}".format(payload['name'],
                                                                              r_data['id']))
                    return OrderedDict({"JP_NAME": payload['name'], "JP_ID": r_data['id']})
                else:
                    print("JP Creation failed")
            else:
                print("Create Request Failed for the JP: {}".format(payload['name']))
                return None
        else:
            print("Create of JP: {} Failed".format(payload['name']))
            return None

    def mark_task_id_official(self, task_id):
        if self.session is not None:
            url = "https://jita.eng.nutanix.com/api/v2/agave_tasks/"+task_id+"/mark_official"
            try:
                r = self.session.put(url, json={},
                                     verify=False, timeout=self.api_call_timeout)
            except Exception as e:
                print("Tasks ID : {} failed to Mark Official due to : {}".format(task_id, str(e)))
            print (r)
            if r.ok:
                r_data = json.loads(r.content)
                if r_data['success']:
                    print("Tasks ID : {}, Marked Official successfully".format(task_id))
                    return "Official_Marked"
                else:
                    print("Tasks ID: {} api call failed".format(task_id))
                    return None
        else:
            print("Cannot Mark task id Official: {}".format(task_id))
            return None

    def mark_jita_tasks_official(self, tasks):
        task_result = dict.fromkeys(tasks)
        if not tasks:
            print("Task List is Empty, nothing to mark oficial..!!")
            return
        else:
            while tasks:
                for task_id in tasks:
                    task_status = self.mark_task_id_official(task_id)
                    task_result[task_id] = task_status
                    tasks.remove(task_id)

    def kill_task_id(self, task_id):
        if self.session is not None:
            url = "https://jita.eng.nutanix.com/api/v2/agave_tasks/" + task_id + "/kill"
            try:
                r = self.session.post(url, json={},
                                      verify=False, timeout=self.api_call_timeout)
            except Exception as e:
                print("Tasks ID : {} failed to kill due to : {}".format(task_id, str(e)))
            if r.ok:
                r_data = json.loads(r.content)
                if r_data['success']:
                    print("Tasks ID : {}, killed successfully".format(task_id))
            else:
                print("Tasks ID: {} api call failed".format(task_id))
        else:
            print("Cannot kill tasks id: {}".format(task_id))

    def kill_jita_tasks(self, tasks):
        task_result = dict.fromkeys(tasks)
        if not tasks:
            print("Task List is Empty, nothing to kill..!!")
            return
        else:
            while tasks:
                for task_id in tasks:
                    task_status = Jita.fetch_status_task_id(task_id)
                    if task_status in ['completed', 'killed']:
                        print("Task ID: {} already in completed state".format(task_id))
                        task_result[task_id] = task_status
                        tasks.remove(task_id)
                    else:
                        self.kill_task_id(task_id)
            print("Tasks Result: {}".format(task_result))

    def validate_job_profile_payload(self):
        pass

    def update_test_set(self):
        pass


if __name__ == '__main__':
    pass
#     task_id = '5cc739837b48b1017b67ba3c'
#     jita = Jita()
# #    jita.mark_task_official(task_id)
# #    jita.fetch_status_task_id(task_id)
#     res = jita.get_jp_name_from_jita_task(task_id)
#     print res['label'], res['_id'], res['email']

#####

