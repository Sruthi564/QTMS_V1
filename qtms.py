import re
import pprint
from jita import Jita
from pprint import pprint
from compatibility_payload import NEW_COMPATIBILITY_PAYLOAD, PE_MATRIX, PC_MATRIX, SAMPLE_COMPATIBILITY_PAYLOAD
from emails import SendEmail


class QTMS(object):
    def __init__(self):
        self.jita = Jita()
        self.tasks = []
        self.catalog_tasks = []
        self.catalog_tasks_link = "https://jita.eng.nutanix.com/results?agave_task_ids="
        self.reg_handedover_tasks = []
        self.reg_handedover_tasks_link = "https://jita.eng.nutanix.com/results?agave_task_ids="
        self.non_reg_handedover_tasks = []
        self.non_reg_handedover_tasks_link = "https://jita.eng.nutanix.com/results?agave_task_ids="
        self.cloned_jps = {}
        self.compatibility_jps = {}
        self.jita_task_link = "https://jita.eng.nutanix.com/results?agave_task_ids="

    # def kill_tasks(self, tasks):
    #     self.jita.kill_jita_tasks(tasks)

    def get_job_profile_payload(self, jp_id):
        payload = self.jita.fetch_job_profile_payload(jp_id)
        print("Job Profile Payload : {}".format(payload))

    def get_job_profile_id(self, jps):
        for jp in jps:
            jp_id = self.jita.get_job_profile_id(jp["JP_NAME"])

    def clone_job_profile(self, jps, payload2, clone_from_branch,
                          clone_to_branch, clone_key):
        local_clone = []
        for jp in jps:
            jp_id = self.jita.get_job_profile_id(jp["JP_NAME"])
            if jp_id is None:
                jp_id = jp["JP_ID"]
            payload1 = self.jita.fetch_job_profile_payload(jp_id)
            clone_jp = self.jita.clone_job_profile(payload1, payload2,
                                                   clone_from_branch, clone_to_branch,
                                                   jp['sub-component'], jp['category'],
                                                   jp['max_dep'])
            if clone_jp is not None:
                local_clone.append(clone_jp)
            else:
                local_clone.append(dict())
        self.cloned_jps[clone_key] = local_clone

    def update_job_profiles(self, jps, payload):
        for jp in jps:
            #jp_id = self.jita.get_job_profile_id(jp["JP_NAME"])
            #if jp_id is None:
            jp_id = jp["JP_ID"]
            for tags in payload['tester_tags']:
                if tags.startswith("max_deployments"):
                    #print "\nTester Tags: {}".format(payload['tester_tags'])
                    payload['tester_tags'].remove(tags)
            payload['tester_tags'].extend(jp["max_dep"])
            #fqa_id = jp.get("FQA", [""])
            # fqa_id = ''
            # if 'emails' in payload.keys():
            #     fqa_id = payload['emails']
            self.jita.update_job_profile_payload(jp_id, jp["JP_NAME"], payload)

    def trigger_job_profile(self, jps, payload):
        for jp in jps:
            print (jp)
            # jp_id = self.jita.get_job_profile_id(jp["JP_NAME"])
            # if jp_id is None:
            #     jp_id = jp["JP_ID"]
            jp_id = jp["JP_ID"]
            for tags in payload['tester_tags']:
                if tags.startswith("max_deployments"):
                    payload['tester_tags'].remove(tags)
            payload['tester_tags'].extend(jp["max_dep"])
            #fqa_id = jp.get("FQA", [""])
            fqa_id = ''
            if 'emails' in payload.keys():
                fqa_id = payload['emails']
            self.jita.trigger_job_profile(jp["JP_NAME"], jp_id, fqa_id, payload, jp['category'], jp['sub-component'])
#        print 'Tasks ids are: {}'.format(self.jita.tasks_ids)

    def send_mail(self, branch, tasks, jita_task_link, email_text=None, email_msg=None, emails=None):
        build_email(branch, tasks, jita_task_link, email_text, email_msg, emails)

    def mark_tasks_official(self, tasks, task_link=True):
        if task_link:
            delimiters = ",", "="
            regexPattern = '|'.join(map(re.escape, delimiters))
            task_to_mark_official = re.split(regexPattern, tasks)[1:]
        else:
            task_to_mark_official = tasks
        self.jita.mark_jita_tasks_official(task_to_mark_official)

    def kill_tasks(self, tasks, task_link=True):
        if task_link:
            delimiters = ",", "="
            regexPattern = '|'.join(map(re.escape, delimiters))
            task_to_kill = re.split(regexPattern, tasks)[1:]
        else:
            task_to_kill = tasks
        self.jita.kill_jita_tasks(task_to_kill)

    def get_tasks_status(self, tasks):
        #print "\nTasks: {}\n".format(tasks)
        overall_tasks_details = {}
        for task_id in tasks:
            task_status = Jita.fetch_status_task_id(task_id[0]['$oid'])
            task_id[0]['task_status'] = task_status
            self.tasks.append(task_id)
            if task_id[0]['sub-component'] == 'catalog':
                self.catalog_tasks.append(task_id)
                self.catalog_tasks_link = self.jita_task_link + str(task_id[0]['$oid']).strip() + ','
                overall_tasks_details['catalog'] = [self.catalog_tasks, self.catalog_tasks_link]
            if task_id[0]['category'] == 'non-reg-handedover':
                self.non_reg_handedover_tasks.append(task_id)
                self.non_reg_handedover_tasks_link = self.non_reg_handedover_tasks_link + str(task_id[0]['$oid']).strip() + ','
                overall_tasks_details['non-reg-handedover'] = [self.non_reg_handedover_tasks, self.non_reg_handedover_tasks_link]
            if task_id[0]['category'] == 'reg-handedover':
                self.reg_handedover_tasks.append(task_id)
                self.reg_handedover_tasks_link = self.reg_handedover_tasks_link + str(task_id[0]['$oid']).strip() + ','
                overall_tasks_details['reg-handedover'] = [self.reg_handedover_tasks, self.reg_handedover_tasks_link]

            self.jita_task_link = self.jita_task_link + str(task_id[0]['$oid']).strip() + ','

        print ("\n ================ Tasks Details ================= \n {}".format(self.tasks))
        print ("\n ================ Overall Task Link ================ \n {}".format(self.jita_task_link[:-1]))

        if self.catalog_tasks:
            self.catalog_tasks_link = self.catalog_tasks_link[:-1]
            print ("\n ================ Catalog Task Link ================ \n {}".format(self.catalog_tasks_link))
        if self.non_reg_handedover_tasks:
            self.non_reg_handedover_tasks_link = self.non_reg_handedover_tasks_link[:-1]
            print ("\n ================ Non-Reg Handedover Tasl Link ================ \n {}".format(self.non_reg_handedover_tasks_link))
        if self.reg_handedover_tasks:
            self.reg_handedover_tasks_link = self.reg_handedover_tasks_link[:-1]
            print ("\n ================ Reg Handedover Task Link ================ \n {}".format(self.reg_handedover_tasks_link))

        #return self.jita_task_link[:-1]
        return overall_tasks_details

    def execute_qtms_ops(self):
        for jita_operation in self.jita_operations:
            if jita_operation["op"] == 'update_job_profile':
                print ("\n ================ Updating Job Profile ================ \n")
                for jp in self.job_profiles:
                    self.update_job_profiles(jp['jps'], jp['payload'])
            if jita_operation["op"] == 'trigger_job_profile':
                for jp in self.job_profiles:
                    self.trigger_job_profile(jp['jps'], jp['payload'])
                jita_tasks = self.get_tasks_status(self.jita.tasks_ids)
                if self.catalog_tasks:
                    branch = self.catalog_tasks[0][0]['branch']
                    #tasks = self.catalog_tasks
                    #jita_task_link = self.catalog_tasks_link
                    emails = [u'alejand.mier@nutanix.com', u'mohammad.parvez@nutanix.com',
                              u'chaitanya.karlekar@nutanix.com',
                              u'guillermo.zapatamond@nutanix.com', u'mladen.drobnjakovic@nutanix.com',
                              u'mohammed@nutanix.com',
                              u'saurabh.dohare@nutanix.com', u'shashank.kumar@nutanix.com',
                              u'suraj.kasi@nutanix.com']
                    email_text = 'Catalog Regression Test Run Details'
                    email_msg = 'Catalog Regression Test Run Details'
                    print ("Sending email for Catalog Regression Test runs: {}".format(self.catalog_tasks_link))
                    mail_instance_catalog = SendEmail(branch, tasks=jita_tasks['catalog'][0], jita_task_link=jita_tasks['catalog'][1],
                                                      email_text=email_text, email_msg=email_msg, emails=emails)
                    mail_instance_catalog.build_email()
                    #self.send_mail(branch, self.catalog_tasks, self.catalog_tasks_link, email_text, email_msg, emails)
                if self.reg_handedover_tasks:
                    branch = self.reg_handedover_tasks[0][0]['branch']
                    #tasks = self.reg_handedover_tasks
                    #jita_task_link = self.reg_handedover_tasks_link
                    emails = ['saurabh.jain@nutanix.com', 'velurusruthi.naidu@nutanix.com', 'ritopa.dey@nutanix.com','jayanthi.r@nutanix.com']
                    email_text = 'Acropolis Regression Reg Handedover Test Run Details'
                    email_msg = 'Acropolis Regression Reg Handedover Test Run Details'
                    print ("Sending email for Reg Handedover Test runs: {}".format(self.reg_handedover_tasks_link))
                    mail_instance_reg_handedover = SendEmail(branch, tasks=jita_tasks['reg-handedover'][0], jita_task_link=jita_tasks['reg-handedover'][1],
                                                      email_text=email_text, email_msg=email_msg, emails=emails)
                    mail_instance_reg_handedover.build_email()
                    #self.send_mail(branch, self.reg_handedover_tasks, self.reg_handedover_tasks_link, email_text, email_msg, emails)
                if self.non_reg_handedover_tasks:
                    branch = self.non_reg_handedover_tasks[0][0]['branch']
                    #tasks = self.non_reg_handedover_tasks
                    #jita_task_link = self.non_reg_handedover_tasks_link
                    emails = ['bhawani.singh@nutanix.com', 'velurusruthi.naidu@nutanix.com', 'ritopa.dey@nutanix.com']
                    email_text = 'Acropolis Regression Non Reg Handedover Test Run Details'
                    email_msg = 'Acropolis Regression Non Reg Handedover Test Run Details'
                    print ("Sending email for Non-Reg Handedover Test runs: {}".format(self.non_reg_handedover_tasks_link))
                    mail_instance_non_reg_handedover = SendEmail(branch, tasks=jita_tasks['non-reg-handedover'][0], jita_task_link=jita_tasks['non-reg-handedover'][1],
                                                      email_text=email_text, email_msg=email_msg, emails=emails)
                    mail_instance_non_reg_handedover.build_email()
                    #self.send_mail(branch, self.non_reg_handedover_tasks, self.non_reg_handedover_tasks_link, email_text, email_msg, emails)

                # if jp['emails'] is not None:
                #     self.send_mail(jp["payload"]['git']['branch'], self.tasks, jita_tasks, jp['emails'])
                # else:
                #     self.send_mail(jp["payload"]['git']['branch'], self.tasks, jita_tasks)

                if self.jita.jps_not_triggered:
                    print ("\n ================ List of Job Profiles Failed to trigger ================ \n {}".format(self.jita.jps_not_triggered))
            if jita_operation["op"] == 'create_compatibility_jps':
                self.create_compatilibility_job_profiles(self.compatibility_matrix, self.component)
            if jita_operation["op"] == 'clone_job_profile':
                print ("\n ================ Performning Clone Operations ================ \n")
                for jp in self.clone_from_jps:
                    #print "JP: {}".format(jp)
                    self.clone_job_profile(jp['jps'], jp['payload'], jita_operation["fromBranch"],
                                           jita_operation["toBranch"], jp['jp_type'])
                print ("\n ================ Jop Profiles Cloned are ================ \n {}".format(self.cloned_jps))
                print ("\n ================ Formatted Output of Cloned Job Profiles ================ \n")
                pprint(self.cloned_jps)

    def create_compatilibility_job_profiles(self, compat_matrix, component):
        jps = []
        for matrix in compat_matrix:
            component_values = ''
            pc_build = ''
            if matrix["pe"] in PE_MATRIX.keys():
                for comp in PE_MATRIX[matrix["pe"]]:
                    if component in comp.keys():
                        component_values = comp
            if matrix["pc"] in PC_MATRIX.keys():
                pc_build = PC_MATRIX[matrix["pc"]]
            new_jp = self.jita.create_compatilibility_job_profiles(component, SAMPLE_COMPATIBILITY_PAYLOAD,
                                                                   NEW_COMPATIBILITY_PAYLOAD,
                                                                   component_values, matrix, pc_build)
            if new_jp is not None:
                jps.append(new_jp)
            else:
                jps.append(dict())
        self.compatibility_jps[component] = jps
        print ("Comaptibility Job Profiles are : {}".format(self.compatibility_jps))



if __name__ == '__main__':
    qtms_execute = QTMS()
    operation = [
#        'update_gold_suite_jps',
#        'trigger_gold_suite_jps',
#        'clone_acropolis_mr',
#        'clone_uhura_mr',
#        'clone_acropolis_lts',
#        'clone_uhura_lts',
#        'update_acropolis_master',
#        'update_uhura_master',
#        'trigger_acropolis_master',
#        'trigger_uhura_master',
#        'update_acropolis_mr',
#        'update_uhura_mr',
#        'trigger_acropolis_mr',
#        'trigger_uhura_mr'
#        'update_acropolis_lts',
#        'update_uhura_lts',
#        'trigger_acropolis_lts',
#        'trigger_uhura_lts'
    ]

###### QTMS for Uhura
    ##### Individual Job Profile
#    JPs = UHURA_JPS_MASTER["NO-PC-WITH-VC"]
#    JPs = ACROPOLIS_JPS_MASTER["GUEST-OS"]
#    qtms_execute.get_job_profile_payload("5ba33ee3114cdb6402394fb0")
#    qtms_execute.get_job_profile_id({"Regression_Acropolis_MTS_Nutest_Guest_OS_5.10"})
#    qtms_execute.get_job_profile_payload('5da59fc17b48b12c0e592b73')
#    qtms_execute.get_job_profile_id(JPs)
#    qtms_execute.get_job_profile_payload('5cb45d4a7b48b1f0b1d52d64')
#    qtms_execute.get_job_profile_payload('5db68d717b48b1f02202a692')
#     tasks = [[{u'$oid': u'5c48a26b7b48b1cce509e785',
#               'jp_name': "Regression_Acropolis_MTS_Nutest_AOS_master_NS",
#               'task_status': 'pending', "FQA": ["dipika.darshan@nutanix.com", "maksim.kalitinenkov@nutanix.com"]}]]
#     task_url = "https://jita.eng.nutanix.com/results?agave_task_ids=5cc1cd527b48b1fc0fdc27dd,5cc1cd577b48b1fc0fdc2942,5cc1cd5b7b48b1fc0fdc294f,5cc1cd5e7b48b1fc0fdc2967"
#
#     qtms_execute.send_mail('master', tasks, task_url)

#    tasks = ['5c5bd3b17b48b190d127e407', '5c48a26b7b48b1cce509e785']
#    qtms_execute.kill_tasks(tasks)
#    qtms_execute.jita.get_jita_testset("AHV_Regression_Uhura_GoldSuite")

    task_url ="https://jita.eng.nutanix.com/results?agave_task_ids=5fbbd2852bc0c444caa0b5ed,5fbbd2852bc0c444caa0b5ed,5fbbd2862bc0c444caa0b5f4,5fbbd2882bc0c444caa0b613,5fbbd28a2bc0c444caa0b61c,5fbbd28c2bc0c444caa0b620,5fbbd28d2bc0c444caa0b628"
    qtms_execute.mark_tasks_official(task_url)
    #qtms_execute.kill_tasks(task_url)

###

