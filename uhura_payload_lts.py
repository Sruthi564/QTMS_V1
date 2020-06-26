NUTEST_BRANCH = u'euphrates-5.5.6-stable'
REL_BRANCH = u'euphrates-5.5.9-stable'


#PC_URL = u'http://endor.dyn.nutanix.com/builds/PC-builds/' + REL_BRANCH + '/'
#PC_COMMIT_ID = '963e97f8a133331ce05435e2e25d2e9f3f975419'


NOS_COMMIT_ID = ""

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

UHURA_PAYLOAD_LTS = dict()
UHURA_PAYLOAD_LTS['tester_tags'] = [u'all', u'v3.1', u'max_deployments__30', u'phx1',
                                    u'sched__phx1', u'rdm__phx1', u'sched__beta',
                                    u'official']

##### Specify Nutest Branch
UHURA_PAYLOAD_LTS['nutest_branch'] = NUTEST_BRANCH
UHURA_PAYLOAD_LTS['test_framework'] = u'nutest'

UHURA_PAYLOAD_LTS[u'emails'] = [u'saurabh.dohare@nutanix.com',
                                u'velurusruthi.naidu@nutanix.com',
                                u'bhawani.singh@nutanix.com']
UHURA_PAYLOAD_LTS['plugins'] = {u'post_run': [
        {u'args': {},
         u'description': u'Sends mail to the recipients.',
         u'stage': u'post_run',
         u'name': u'EmailPlugin'}]
}

UHURA_PAYLOAD_LTS['build_selection'] = USE_NOS_BY_SMOKE_PASSED
#UHURA_PAYLOAD_LTS['build_selection'] = USE_NOS_BY_SMOKE_PASSED

UHURA_PAYLOAD_LTS['git'] = {
        u'repo': u'main',
        u'branch': REL_BRANCH
}
UHURA_PAYLOAD_LTS['cluster_selection'] = {
        u'pool_name': [u'AHV_NODE_POOL_OSL'],
        u'by_node_pool': True
}
UHURA_PAYLOAD_LTS[u'requested_hardware'] = {
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
UHURA_PAYLOAD_LTS['resource_manager_json'] = dict(PRISM_CENTRAL={
    u'build': {
        u'nos_build_url': ''
    }
})
UHURA_PAYLOAD_PC_LTS = UHURA_PAYLOAD_LTS
UHURA_PAYLOAD_NO_PC_NO_VC_LTS = {k: v for (k, v) in UHURA_PAYLOAD_LTS.items() if k != 'resource_manager_json'}
UHURA_PAYLOAD_NO_PC_WITH_VC_LTS = UHURA_PAYLOAD_NO_PC_NO_VC_LTS.copy()
UHURA_PAYLOAD_NO_PC_WITH_VC_LTS[u'requested_hardware'] = {
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
        u'redundancy_factor': u'default',
        u'secondary_datacenters': {
            u'vsphere': [u'10.41.25.232']
        },
        u'hypervisor_url': ''
    }
}
UHURA_PAYLOAD_NS_WITH_VC_LTS = UHURA_PAYLOAD_NO_PC_WITH_VC_LTS.copy()
UHURA_PAYLOAD_NS_NO_VC_LTS = UHURA_PAYLOAD_NO_PC_NO_VC_LTS.copy()
UHURA_PAYLOAD_NS_WITH_VC_LTS['cluster_selection'] = {
        u'pool_name': [u'AHV_NODE_POOL_OSL'],
        u'by_node_pool': True
}
UHURA_PAYLOAD_NS_NO_VC_LTS['cluster_selection'] = {
        u'pool_name': [u'AHV_NODE_POOL_OSL'],
        u'by_node_pool': True
}
