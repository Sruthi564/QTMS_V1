NUTEST_BRANCH = u'euphrates-5.17-stable'
REL_BRANCH = u'euphrates-5.17.0.3-stable'
OBELIX_BRANCH = u'dogmatix_5.17'


#POOL_NAME = [u'AHV-REG-NODE-POOL-MASTER']
GPU_POOL_NAME = [u'ahv-gpu-regression']
POOL_NAME = [u'AHV_NODE_POOL_OSL']


#BUILD_TYPE = 'opt'
BUILD_TYPE = 'release'

#NOS_URL = u'http://endor.dyn.nutanix.com/builds/nos-builds/euphrates-5.11.2.2-stable/4c36cc098ebbca702e1c4c00ed989844091d5eb0/opt/tar/nutanix_installer_package-opt-euphrates-5.11.2.2-stable-4c36cc098ebbca702e1c4c00ed989844091d5eb0.tar.gz'
NOS_URL = ''

PC_URL = u'http://endor.dyn.nutanix.com/builds/PC-builds/' + REL_BRANCH + '/'
#PC_URL = u'http://endor.dyn.nutanix.com/builds/nos-builds/euphrates-5.16.1.1-stable/9ad6f1b6766a4d6e5076548e74bef04dc6d42fa3-PC/release/tar/nutanix_installer_package_pc-release-euphrates-5.16.1.1-stable-9ad6f1b6766a4d6e5076548e74bef04dc6d42fa3.tar.gz'
PC_COMMIT_ID = '171557c7b075e1ae5185e280939663bee781a8ce'


NOS_COMMIT_ID = "171557c7b075e1ae5185e280939663bee781a8ce"



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


GOLD_SUITE_PAYLOAD = dict()

#GOLD_SUITE_PAYLOAD['tester_tags'] = [u'v3.1', u'max_deployments__30', u'official']

GOLD_SUITE_PAYLOAD['tester_tags'] = [u'v3.1', u'max_deployments__7']


##### Specify Nutest Branch
GOLD_SUITE_PAYLOAD['nutest_branch'] = NUTEST_BRANCH
GOLD_SUITE_PAYLOAD['test_framework'] = u'nutest'

GOLD_SUITE_PAYLOAD['patch_url'] = ''
GOLD_SUITE_PAYLOAD['scheduling_options'] = {
    u'optimize_scheduling': True,
    u'force_imaging': False,
    u'task_priority': 80,
    u'skip_resource_spec_match': False,
    u'upgrade': False,
    u'retry_imaging': 2,
    u'check_image_compatibility': True
}
GOLD_SUITE_PAYLOAD['nutest_commit'] = None


GOLD_SUITE_PAYLOAD[u'emails'] = [u'velurusruthi.naidu@nutanix.com',
                                 u'bhawani.singh@nutanix.com',
                                 u'saurabh.dohare@nutanix.com'
                                ]


GOLD_SUITE_PAYLOAD['plugins'] = {u'post_run': [
        {u'args': {},
         u'description': u'Sends mail to the recipients.',
         u'stage': u'post_run',
         u'name': u'EmailPlugin'}]
}


GOLD_SUITE_PAYLOAD['build_selection'] = USE_NOS_BY_COMMIT_ID

##### Specify Patch Release Branch
GOLD_SUITE_PAYLOAD['git'] = {
        u'repo': u'main',
        u'branch': REL_BRANCH
}


GOLD_SUITE_PAYLOAD['cluster_selection'] = {
        u'pool_name': POOL_NAME,
        u'by_node_pool': True
}
GOLD_SUITE_PAYLOAD[u'requested_hardware'] = {
    u'hypervisor_version': u'branch_symlink',
    u'hypervisor': u'kvm',
    u'imaging_options': {
        u'datacenter': {
            u'hyperv': {},
            u'kvm': {},
            u'vsphere': {},
            u'use_host_names': False
        },
        u'min_ram': u'15',
        u'nos_url': NOS_URL,
        u'redundancy_factor': u'default',
        u'secondary_datacenters': {
            u'vsphere': {}
        },
        u'hypervisor_url': ''
    }
}
GOLD_SUITE_PAYLOAD['resource_manager_json'] = dict(PRISM_CENTRAL={
    u'build': {
        u'nos_build_url': PC_URL + PC_COMMIT_ID + '/' + BUILD_TYPE
                          + '/'
    }
})

GOLD_SUITE_PAYLOAD_PC = GOLD_SUITE_PAYLOAD.copy()
GOLD_SUITE_PAYLOAD_NO_PC = {k: v for (k, v) in GOLD_SUITE_PAYLOAD.items() if k != 'resource_manager_json'}
GOLD_SUITE_PAYLOAD_UHURA = GOLD_SUITE_PAYLOAD_PC.copy()
GOLD_SUITE_PAYLOAD_UHURA[u'requested_hardware'] = {
    u'hypervisor_version': u'6.5.0',
    u'hypervisor': u'vsphere',
    u'imaging_options': {
        u'datacenter': {
            u'hyperv': {},
            u'kvm': {},
            u'vsphere': {u'vcenter': u'10.41.25.40'},
            u'use_host_names': False
        },
        u'min_ram': u'15',
        u'nos_url': NOS_URL,
        u'redundancy_factor': u'default',
        u'secondary_datacenters': {
            u'vsphere': {
                u'vcenters': [u'10.41.25.232']
            }
        },
        u'hypervisor_url': ''
    }
}
GOLD_SUITE_PAYLOAD_GPU = GOLD_SUITE_PAYLOAD.copy()

# GOLD_SUITE_PAYLOAD_GPU['cluster_selection'] = {
#     u'cluster_names': [u'gardenia'],
#     u'by_names': True
# }


# GOLD_SUITE_PAYLOAD_GPU['cluster_selection'] = {
#         u'pool_name': GPU_POOL_NAME,
#         u'by_node_pool': True
# }

GOLD_SUITE_PAYLOAD_GPU['cluster_selection'] = {
        u'pool_name': GPU_POOL_NAME,
        u'by_node_pool': True
}