
# NUTEST_BRANCH = u'euphrates-5.10-stable'
# AOS_REL_BRANCH = u'euphrates-5.10.6-stable'
# PC_REL_BRANCH = u'euphrates-5.10.6-stable'
# OBELIX_BRANCH = u'obelix_5.10.6'

#NUTEST_BRANCH = u'euphrates-5.10-stable'
#AOS_REL_BRANCH = u'euphrates-5.10.7-stable'
#PC_REL_BRANCH = u'euphrates-5.10.7-stable'
#OBELIX_BRANCH = u'obelix_5.10.7'

#NUTEST_BRANCH = u'euphrates-5.11-stable'
#AOS_REL_BRANCH = u'euphrates-5.11.1-stable'
#PC_REL_BRANCH = u'euphrates-5.11.1-stable'
#OBELIX_BRANCH = u'obelix_5.11.1'

#NUTEST_BRANCH = u'euphrates-5.10-stable'
#AOS_REL_BRANCH = u'euphrates-5.10.11-stable'
#PC_REL_BRANCH = u'euphrates-5.10.11-stable'
#OBELIX_BRANCH = u'obelix'

#NUTEST_BRANCH = u'euphrates-5.15-stable'
#AOS_REL_BRANCH = u'euphrates-5.15-stable'
#PC_REL_BRANCH = u'euphrates-5.11.3-stable'
#OBELIX_BRANCH = u'obelix'

#NUTEST_BRANCH = u'euphrates-5.16-stable'
#AOS_REL_BRANCH = u'euphrates-5.16.1-stable'
#PC_REL_BRANCH = u'euphrates-5.16.1-stable'
#OBELIX_BRANCH = u'dogmatix'

#NUTEST_BRANCH = u'euphrates-5.15-stable'
#AOS_REL_BRANCH = u'euphrates-5.15.2-stable'
#PC_REL_BRANCH = u'euphrates-5.15.2-stable'
#OBELIX_BRANCH = u'obelix'

NUTEST_BRANCH = u'euphrates-5.15-stable'
AOS_REL_BRANCH = u'euphrates-5.15.4-stable'
PC_REL_BRANCH = u'euphrates-5.15.4-stable'
OBELIX_BRANCH = u'obelix_5.15'

#POOL_NAME = [u'AHV-REG-NODE-POOL-MASTER']
GPU_POOL_NAME = [u'ahv-gpu-regression']
POOL_NAME = [u'AHV_NODE_POOL_OSL']

BUILD_TYPE = 'opt'
#BUILD_TYPE = 'release'

NOS_URL = ''
#NOS_URL = 'http://endor.dyn.nutanix.com/releases/Euphrates-5.15-stable-RC1/f322bb1e20845aadc476b89eaf0647397e8a3222/x86_64/opt/tar/nutanix_installer_package-opt-euphrates-5.15-stable-f322bb1e20845aadc476b89eaf0647397e8a3222-x86_64.tar.gz'

#HYPERVISOR_BUILD_URL = 'http://endor.dyn.nutanix.com/builds/ahv-builds/20190916.231/iso/AHV-DVD-x86_64-el7.nutanix.20190916.231.iso'

HYPERVISOR_BUILD_URL = ''
FOUNDATION_BUILD_URL = ''
#FOUNDATION_BUILD_URL = u'http://endor.dyn.nutanix.com/builds/foundation-builds/4.5/foundation-4.5-90-88e38e12-universal-release.x86_64.tar.gz'

PC_URL = u'http://endor.dyn.nutanix.com/builds/PC-builds/' + PC_REL_BRANCH + '/'
PC_COMMIT_ID = '3218a31e15584e368dc4c9b7abc4d99da585c8d2'

NOS_COMMIT_ID = '3218a31e15584e368dc4c9b7abc4d99da585c8d2'


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

UHURA_PAYLOAD_MINOR_REL = dict()
# UHURA_PAYLOAD_MINOR_REL['tester_tags'] = [u'all', u'v3.1', u'max_deployments__30', u'phx1',
#                                           u'sched__phx1', u'rdm__phx1', u'sched__beta',
#                                           u'official']
UHURA_PAYLOAD_MINOR_REL['tester_tags'] = [u'v3.1', u'max_deployments__7', u'official']
#UHURA_PAYLOAD_MINOR_REL['tester_tags'] = [u'v3.1', u'max_deployments__7']


UHURA_PAYLOAD_MINOR_REL['patch_url'] = ''

UHURA_PAYLOAD_MINOR_REL['scheduling_options'] = {
    u'optimize_scheduling': True,
    u'force_imaging': False,
    u'task_priority': 80,
    u'skip_resource_spec_match': False,
    u'upgrade': False,
    u'retry_imaging': 2,
    u'check_image_compatibility': True
}


##### Specify Nutest Branch
UHURA_PAYLOAD_MINOR_REL['nutest_branch'] = NUTEST_BRANCH
UHURA_PAYLOAD_MINOR_REL['nutest_commit'] = ''


UHURA_PAYLOAD_MINOR_REL['test_framework'] = u'nutest'

UHURA_PAYLOAD_MINOR_REL[u'emails'] = [u'velurusruthi.naidu@nutanix.com',
                                      u'bhawani.singh@nutanix.com']

UHURA_PAYLOAD_MINOR_REL['plugins'] = {u'post_run': [
        {u'args': {},
         u'description': u'Sends mail to the recipients.',
         u'stage': u'post_run',
         u'name': u'EmailPlugin'}]
}

UHURA_PAYLOAD_MINOR_REL['build_selection'] = USE_NOS_BY_COMMIT_ID
#UHURA_PAYLOAD_MINOR_REL['build_selection'] = USE_NOS_BY_SMOKE_PASSED

UHURA_PAYLOAD_MINOR_REL['git'] = {
        u'repo': u'main',
        u'branch': AOS_REL_BRANCH
}
UHURA_PAYLOAD_MINOR_REL['cluster_selection'] = {
        u'pool_name': [u'AHV_NODE_POOL_OSL'],
        u'by_node_pool': True
}
### Around line 130-148
UHURA_PAYLOAD_MINOR_REL[u'requested_hardware'] = {
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
        u'nos_url': NOS_URL,
        u'secondary_datacenters': {
            u'vsphere': {}
        },
        u'hypervisor_url': HYPERVISOR_BUILD_URL
    }
}
UHURA_PAYLOAD_MINOR_REL['resource_manager_json'] = dict(PRISM_CENTRAL={
    u'build': {
        u'nos_build_url': PC_URL + PC_COMMIT_ID + '/' + BUILD_TYPE + '/'
    }
})
UHURA_PAYLOAD_PC_MINOR_REL = UHURA_PAYLOAD_MINOR_REL
UHURA_PAYLOAD_NO_PC_NO_VC_MINOR_REL = {k: v for (k, v) in UHURA_PAYLOAD_MINOR_REL.items() if k != 'resource_manager_json'}
UHURA_PAYLOAD_NO_PC_WITH_VC_MINOR_REL = UHURA_PAYLOAD_NO_PC_NO_VC_MINOR_REL.copy()
UHURA_PAYLOAD_NO_PC_WITH_VC_MINOR_REL[u'requested_hardware'] = {
    u'hypervisor_version': u'6.7.0',
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
            u'vsphere': {
                u'vcenters': [u'10.41.28.124']
            }
        },
        u'hypervisor_url': ''
    }
}
UHURA_PAYLOAD_NS_WITH_VC_MINOR_REL = UHURA_PAYLOAD_NO_PC_WITH_VC_MINOR_REL.copy()
UHURA_PAYLOAD_NS_NO_VC_MINOR_REL = UHURA_PAYLOAD_NO_PC_NO_VC_MINOR_REL.copy()
UHURA_PAYLOAD_NS_WITH_VC_MINOR_REL['cluster_selection'] = {
        u'pool_name': [u'AHV_NODE_POOL_OSL'],
        u'by_node_pool': True
}
UHURA_PAYLOAD_NS_NO_VC_MINOR_REL['cluster_selection'] = {
        u'pool_name': [u'AHV_NODE_POOL_OSL'],
        u'by_node_pool': True
}



