NUTEST_BRANCH = u'master'
AOS_REL_BRANCH = u'master'
PC_REL_BRANCH = u'master'


#POOL_NAME = [u'AHV-REG-NODE-POOL-MASTER']
POOL_NAME = [u'AHV_NODE_POOL_OSL']

PC_URL = u'http://endor.dyn.nutanix.com/builds/PC-builds/' + PC_REL_BRANCH + '/'
PC_COMMIT_ID = '1e08eac6e371f6658dfc95a516cd876ce7b7b035'

NOS_COMMIT_ID = "1e08eac6e371f6658dfc95a516cd876ce7b7b035"



NOS_URL = ''

#HYPERVISOR_URL = 'http://endor.dyn.nutanix.com/isos/vmware/vsphere/6.5U1/VMware-VMvisor-Installer-6.5.0.update01-5969303.x86_64.iso'

HYPERVISOR_URL = ''

FOUNDATION_BUILD_URL = ''
#FOUNDATION_BUILD_URL = u'http://endor.dyn.nutanix.com/builds/foundation-builds/4.5/foundation-4.5-90-88e38e12-universal-release.x86_64.tar.gz'

#SKIP_COMMIT_VALIDATION = u'on'
SKIP_COMMIT_VALIDATION = False


#BUILD_TYPE = 'opt'
BUILD_TYPE = 'release'

USE_NOS_BY_COMMIT_ID = {
    u'build_type': BUILD_TYPE,
    u'by_commit_id': True,
    u'commit_id': NOS_COMMIT_ID,
    u'use_stable_agave_commit': False,
    u'use_stable_nutest_commit': False
}

USE_NOS_BY_SMOKE_PASSED = {
        u'use_stable_nutest_commit': False,
        u'by_latest_smoked': True,
        u'build_type': BUILD_TYPE,
        u'use_stable_agave_commit': False
}
UHURA_PAYLOAD_MASTER = dict()
# UHURA_PAYLOAD_MASTER['tester_tags'] = [u'all', u'v3.1', u'max_deployments__30', u'phx1',
#                                        u'sched__phx1', u'rdm__phx1', u'sched__alpha',
#                                        u'official']

UHURA_PAYLOAD_MASTER['tester_tags'] = [u'v3.1', u'max_deployments__7', u'official']
#UHURA_PAYLOAD_MASTER['tester_tags'] = [u'v3.1', u'max_deployments__7']

##### Specify Nutest Branch
UHURA_PAYLOAD_MASTER['nutest_branch'] = u'master'
UHURA_PAYLOAD_MASTER['test_framework'] = u'nutest'

#UHURA_PAYLOAD_MASTER['nutest_commit'] = ''


UHURA_PAYLOAD_MASTER[u'emails'] = [u'velurusruthi.naidu@nutanix.com',
                                   u'bhawani.singh@nutanix.com']


UHURA_PAYLOAD_MASTER['scheduling_options'] = {
    u'optimize_scheduling': True,
    u'force_imaging': False,
    u'task_priority': 80,
    u'skip_resource_spec_match': False,
    u'upgrade': False,
    u'retry_imaging': 2,
    u'check_image_compatibility': True
}

UHURA_PAYLOAD_MASTER['patch_url'] = ''

UHURA_PAYLOAD_MASTER['plugins'] = {u'post_run': [
           {u'args': {},
            u'description': u'Sends mail to the recipients.',
            u'stage': u'post_run',
            u'name': u'EmailPlugin'}
        ],
         u'pre_run': []
}

# UHURA_PAYLOAD_MASTER['plugins'] = {u'post_run': [
#         {u'args': {},
#          u'description': u'Sends mail to the recipients.',
#          u'stage': u'post_run',
#          u'name': u'EmailPlugin'},
#         {u'args': {u'xml_file': None, u'services': [u'uhura'], u'db_password': None,
#                    u'enable_traceability': False,
#                    u'db_coverage_ip': u'drt-rlb-mongo-codecoverage-prod-1.corp.nutanix.com', u'port': 27017,
#                    u'db_name': u'cc', u'db_username': None, u'collection_name': u'code_coverage',
#                    u'local_mount': u'/home/nutanix/code_coverage/python', u'pycov_options': [u'-i uhura',
#                                                                                              ],
#                    u'tool_name': u'pycov'},
#          u'description': u'Computes code coverage data for a given NOS service in python source code.',
#          u'stage': u'post_run', u'name': u'CodeCoverageComputePythonPostPlugin'}],
#          u'pre_run': [
#             {u'args': {u'xml_file': None, u'services': [u'uhura'], u'enable_traceability': False,
#                        u'nfs_filer_location': u'10.53.192.66:/volume1/code_coverage/python',
#                        u'pycov_location': u'http://10.4.16.50/home/rachit.sinha/python_coverage/pycov',
#                        u'local_mount': u'/home/nutanix/code_coverage/python', u'pycov_options': [u'-i uhura',
#                                                                                                  ],
#                        u'tool_name': u'pycov'},
#              u'description': u'Computes code coverage data for a given NOS service in python source code.',
#              u'stage': u'pre_run',
#              u'name': u'CodeCoverageComputePythonPrePlugin'}]
# }

UHURA_PAYLOAD_MASTER['build_selection'] = USE_NOS_BY_COMMIT_ID
##### Specify Release Branch
UHURA_PAYLOAD_MASTER['git'] = {
        u'repo': u'main',
        u'branch': AOS_REL_BRANCH
}
UHURA_PAYLOAD_MASTER['cluster_selection'] = {
        u'pool_name': POOL_NAME,
        u'by_node_pool': True
}
UHURA_PAYLOAD_MASTER[u'requested_hardware'] = {
    u'hypervisor_version': u'branch_symlink',
    u'hypervisor': u'kvm',
    u'imaging_options': {
        u'datacenter': {
            u'hyperv': {},
            u'kvm': {},
            u'vsphere': {},
            u'use_host_names': False
        },
        u'foundation_build_url': FOUNDATION_BUILD_URL,
        u'min_ram': u'15',
        u'redundancy_factor': u'default',
        u'secondary_datacenters': {
            u'vsphere': {}
        },
        u'hypervisor_url': ''
    }
}
UHURA_PAYLOAD_MASTER['resource_manager_json'] = dict(PRISM_CENTRAL={
    u'build': {
        u'nos_build_url': PC_URL + PC_COMMIT_ID + '/' + BUILD_TYPE + '/'
    }
})

UHURA_PAYLOAD_PC_MASTER = UHURA_PAYLOAD_MASTER
UHURA_PAYLOAD_NO_PC_NO_VC_MASTER = {k: v for (k, v) in UHURA_PAYLOAD_MASTER.items() if k != 'resource_manager_json'}
UHURA_PAYLOAD_NO_PC_WITH_VC_MASTER = UHURA_PAYLOAD_NO_PC_NO_VC_MASTER.copy()
UHURA_PAYLOAD_NO_PC_WITH_VC_MASTER[u'requested_hardware'] = {
    u'hypervisor_version': u'6.7.0',
    u'hypervisor': u'vsphere',
    u'imaging_options': {
        u'datacenter': {
            u'hyperv': {},
            u'kvm': {},
            u'vsphere': {u'vcenter': u'10.41.25.40'},
            u'use_host_names': False
        },
        u'foundation_build_url': FOUNDATION_BUILD_URL,
        u'min_ram': u'15',
        u'redundancy_factor': u'default',
        u'secondary_datacenters': {
            u'vsphere': {
                u'vcenters': [u'10.41.28.124']
            }
        },
        u'hypervisor_url': ''
    }
}
UHURA_PAYLOAD_NS_WITH_VC_MASTER = UHURA_PAYLOAD_NO_PC_WITH_VC_MASTER.copy()
UHURA_PAYLOAD_NS_NO_VC_MASTER = UHURA_PAYLOAD_NO_PC_NO_VC_MASTER.copy()
UHURA_PAYLOAD_NS_WITH_VC_MASTER['cluster_selection'] = {
        u'pool_name': POOL_NAME,
        u'by_node_pool': True
}
UHURA_PAYLOAD_NS_NO_VC_MASTER['cluster_selection'] = {
        u'pool_name': POOL_NAME,
        u'by_node_pool': True
}
