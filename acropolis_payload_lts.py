NUTEST_BRANCH = u'euphrates-5.5.6-stable'
REL_BRANCH = u'euphrates-5.5.9-stable'
OBELIX_BRANCH = u'obelix_5.5.9'

#PC_URL = u'http://endor.dyn.nutanix.com/builds/PC-builds/' + REL_BRANCH + '/'
#PC_COMMIT_ID = '4494c4e0c282fa42e39b0504f7d762974daaffbb'


NOS_COMMIT_ID = "d22074528ab34314caadb9b7edaa63dd646e256d"

USE_NOS_BY_COMMIT_ID = {
    u'build_type': u'release',
    u'by_commit_id': True,
    u'commit_id': NOS_COMMIT_ID,
    u'use_stable_agave_commit': False,
    u'use_stable_nutest_commit': False
}
USE_NOS_BY_SMOKE_PASSED = {
        u'use_stable_nutest_commit': False,
        u'by_latest_smoked': True,
        u'build_type': u'release',
        u'use_stable_agave_commit': False
}


ACROPOLIS_PAYLOAD_LTS = dict()
ACROPOLIS_PAYLOAD_LTS['tester_tags'] = [u'all', u'v3.1', u'max_deployments__30', u'phx1',
                                        u'sched__phx1', u'rdm__phx1', u'sched__beta',
                                        u'official']
##### Specify Nutest Branch
ACROPOLIS_PAYLOAD_LTS['nutest_branch'] = NUTEST_BRANCH
ACROPOLIS_PAYLOAD_LTS['test_framework'] = u'nutest'
ACROPOLIS_PAYLOAD_LTS[u'emails'] = [u'saurabh.dohare@nutanix.com',
                                    u'velurusruthi.naidu@nutanix.com',
                                    u'bhawani.singh@nutanix.com']

ACROPOLIS_PAYLOAD_LTS['plugins'] = {u'post_run': [
        {u'args': {},
         u'description': u'Sends mail to the recipients.',
         u'stage': u'post_run',
         u'name': u'EmailPlugin'}]
}

ACROPOLIS_PAYLOAD_LTS['build_selection'] = USE_NOS_BY_COMMIT_ID
#ACROPOLIS_PAYLOAD_LTS['build_selection'] = USE_NOS_BY_SMOKE_PASSED

ACROPOLIS_PAYLOAD_LTS['git'] = {
        u'repo': u'main',
        u'branch': REL_BRANCH
}
ACROPOLIS_PAYLOAD_LTS['cluster_selection'] = {
        u'pool_name': [u'AHV_NODE_POOL_OSL'],
        u'by_node_pool': True
}
ACROPOLIS_PAYLOAD_LTS[u'requested_hardware'] = {
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
        u'redundancy_factor': u'default',
        u'secondary_datacenters': {
            u'vsphere': {}
        },
        u'hypervisor_url': ''
    }
}
ACROPOLIS_PAYLOAD_LTS['resource_manager_json'] = dict(PRISM_CENTRAL={
    u'build': {
        u'nos_build_url': ''
    }
})
ACROPOLIS_PAYLOAD_PC_LTS = ACROPOLIS_PAYLOAD_LTS
ACROPOLIS_PAYLOAD_NO_PC_LTS = {k: v for (k, v) in ACROPOLIS_PAYLOAD_LTS.items() if k != 'resource_manager_json'}
ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_LTS = ACROPOLIS_PAYLOAD_NO_PC_LTS.copy()
ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_LTS['plugins'] = {u'post_run': [
        {u'args': {},
         u'description': u'Sends mail to the recipients.',
         u'stage': u'post_run',
         u'name': u'EmailPlugin'},
        {u'args': {u'branch': OBELIX_BRANCH},
         u'description': u'Updates the branch info of the test result document with the info provided in args',
         u'name': u'UpdateBranchPlugin',
         u'stage': u'post_run'}
        ]
}
ACROPOLIS_PAYLOAD_GPU_LTS = ACROPOLIS_PAYLOAD_NO_PC_LTS.copy()
ACROPOLIS_PAYLOAD_GPU_LTS['cluster_selection'] = {
    u'cluster_names': [u'gardenia'],
    u'by_names': True
}
ACROPOLIS_PAYLOAD_VNUMA_LTS = ACROPOLIS_PAYLOAD_NO_PC_LTS.copy()
ACROPOLIS_PAYLOAD_VNUMA_LTS['cluster_selection'] = {
    u'cluster_names': [u'cottonwood'],
    u'by_names': True
}
ACROPOLIS_PAYLOAD_NO_PC_HA_LTS = ACROPOLIS_PAYLOAD_NO_PC_LTS.copy()
ACROPOLIS_PAYLOAD_NO_PC_HA_LTS[u'requested_hardware'] = {
    u'hypervisor_version': u'branch_symlink',
    u'hypervisor': u'kvm',
    u'imaging_options': {
        u'datacenter': {
            u'hyperv': {},
            u'kvm': {},
            u'vsphere': {},
            u'use_host_names': False
        },
        u'min_ram': u'16',
        u'redundancy_factor': u'3',
        u'secondary_datacenters': {
            u'vsphere': {}
        },
        u'hypervisor_url': ''
    }
}

