# NUTEST_BRANCH = u'euphrates-5.11-stable'
# AOS_REL_BRANCH = u'euphrates-5.11-stable'
# PC_REL_BRANCH = u'euphrates-5.11-stable'


#NUTEST_BRANCH = u'euphrates-5.12-stable'
#AOS_REL_BRANCH = u'euphrates-5.12-stable'
#PC_REL_BRANCH = u'euphrates-5.12-stable'fe408330e561dd638d36115ec3b79eb80ccfa1aa

#NUTEST_BRANCH = u'euphrates-5.17-stable'
#AOS_REL_BRANCH = u'euphrates-5.17-stable'
#PC_REL_BRANCH = u'euphrates-5.17-stable'

NUTEST_BRANCH = u'euphrates-5.19-stable'
AOS_REL_BRANCH = u'euphrates-5.19.1-stable'
PC_REL_BRANCH = u'euphrates-5.19-stable-pc-1'

#POOL_NAME = [u'AHV-REG-NODE-POOL-MASTER']
GPU_POOL_NAME = [u'ahv-gpu-regression']
POOL_NAME = [u'AHV_NODE_POOL_OSL']

#BUILD_TYPE = 'opt'
BUILD_TYPE = 'release'

#NOS_URL = "http://phx-ep-filer-build-prod-1.corp.nutanix.com/nos-builds/euphrates-5.10.3.1-stable/655d4def34bf18785782f2adb8cdd5f8457d1fe3/release/tar/nutanix_installer_package-release-euphrates-5.10.3.1-stable-655d4def34bf18785782f2adb8cdd5f8457d1fe3.tar.gz"
NOS_URL = ''

PC_URL = u'http://endor.dyn.nutanix.com/builds/PC-builds/' + PC_REL_BRANCH + '/'
PC_COMMIT_ID = 'd16f9f491e077eb8f1d7382ed37ebc8cb736513d'

NOS_COMMIT_ID = '20bdb87735f6e7cd227572085854461932b7af6c'



HYPERVISOR_URL = ''
#HYPERVISOR_URL = u'http://endor.dyn.nutanix.com/builds/ahv-builds/20190308.101258/iso/AHV-DVD-x86_64-el7.nutanix.20190308.101258.iso'



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

UHURA_PAYLOAD_MAJOR_REL = dict()
# UHURA_PAYLOAD_MAJOR_REL['tester_tags'] = [u'all', u'v3.1', u'max_deployments__30', u'phx1',
#                                           u'sched__phx1', u'rdm__phx1', u'sched__beta',
#                                           u'official']
UHURA_PAYLOAD_MAJOR_REL['tester_tags'] = [u'v3.1', u'max_deployments__7', u'official']


##### Specify Nutest Branch
UHURA_PAYLOAD_MAJOR_REL['nutest_branch'] = NUTEST_BRANCH
UHURA_PAYLOAD_MAJOR_REL['test_framework'] = u'nutest'

UHURA_PAYLOAD_MAJOR_REL['patch_url'] = ''

UHURA_PAYLOAD_MAJOR_REL[u'emails'] = [u'velurusruthi.naidu@nutanix.com',
                                      u'bhawani.singh@nutanix.com']
UHURA_PAYLOAD_MAJOR_REL['plugins'] = {u'post_run': [
        {u'args': {},
         u'description': u'Sends mail to the recipients.',
         u'stage': u'post_run',
         u'name': u'EmailPlugin'}]
}


UHURA_PAYLOAD_MAJOR_REL['scheduling_options'] = {
    u'optimize_scheduling': True,
    u'force_imaging': False,
    u'task_priority': 80,
    u'skip_resource_spec_match': False,
    u'upgrade': False,
    u'retry_imaging': 2,
    u'check_image_compatibility': True
}

UHURA_PAYLOAD_MAJOR_REL['build_selection'] = USE_NOS_BY_COMMIT_ID
#UHURA_PAYLOAD_MAJOR_REL['build_selection'] = USE_NOS_BY_SMOKE_PASSED

UHURA_PAYLOAD_MAJOR_REL['git'] = {
        u'repo': u'main',
        u'branch': AOS_REL_BRANCH
}
UHURA_PAYLOAD_MAJOR_REL['cluster_selection'] = {
        u'pool_name': [u'AHV_NODE_POOL_OSL'],
        u'by_node_pool': True
}
UHURA_PAYLOAD_MAJOR_REL[u'requested_hardware'] = {
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
        u'hypervisor_url': HYPERVISOR_URL
    }
}
UHURA_PAYLOAD_MAJOR_REL['resource_manager_json'] = dict(PRISM_CENTRAL={
    u'build': {
        u'nos_build_url': PC_URL + PC_COMMIT_ID + '/' + BUILD_TYPE + '/'
    }
})
UHURA_PAYLOAD_PC_MAJOR_REL = UHURA_PAYLOAD_MAJOR_REL
UHURA_PAYLOAD_PC_MAJOR_REL['services'] = [u'NOS', u'PC']

UHURA_PAYLOAD_ERGON_PC_MAJOR_REL = UHURA_PAYLOAD_PC_MAJOR_REL.copy()
UHURA_PAYLOAD_ERGON_PC_MAJOR_REL[u'requested_hardware'] = {
    u'hypervisor_version': None,
    u'hypervisor': None,
    u'imaging_options': {
        u'datacenter': {
            u'hyperv': {},
            u'kvm': {},
            u'vsphere': {},
            u'use_host_names': False
        },
        u'min_host_cpu_cores': 6,
        u'min_host_gb_ram': 30,
        u'nos_url': NOS_URL,
        u'redundancy_factor': u'default',
        u'secondary_datacenters': {
            u'vsphere': {}
        },
        u'hypervisor_url': ''
    }
}

UHURA_PAYLOAD_NO_PC_NO_VC_MAJOR_REL = {k: v for (k, v) in UHURA_PAYLOAD_MAJOR_REL.items() if k != 'resource_manager_json'}
UHURA_PAYLOAD_NO_PC_NO_VC_MAJOR_REL['services'] = [u'NOS']
UHURA_PAYLOAD_NO_PC_NO_VC_MAJOR_REL['resource_manager_json'] = dict()
UHURA_PAYLOAD_NO_PC_WITH_VC_MAJOR_REL = UHURA_PAYLOAD_NO_PC_NO_VC_MAJOR_REL.copy()
UHURA_PAYLOAD_NO_PC_WITH_VC_MAJOR_REL[u'requested_hardware'] = {
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
        u'nos_url': NOS_URL,
        u'redundancy_factor': u'default',
        u'secondary_datacenters': {
            u'vsphere': {
                u'vcenters': [u'10.41.28.124']
            }
        },
        u'hypervisor_url': HYPERVISOR_URL
    }
}
UHURA_PAYLOAD_NS_WITH_VC_MAJOR_REL = UHURA_PAYLOAD_NO_PC_WITH_VC_MAJOR_REL.copy()
UHURA_PAYLOAD_NS_NO_VC_MAJOR_REL = UHURA_PAYLOAD_NO_PC_NO_VC_MAJOR_REL.copy()
UHURA_PAYLOAD_NS_WITH_VC_MAJOR_REL['cluster_selection'] = {
        u'pool_name': [u'AHV_NODE_POOL_OSL'],
        u'by_node_pool': True
}
UHURA_PAYLOAD_NS_NO_VC_MAJOR_REL['cluster_selection'] = {
        u'pool_name': [u'AHV_NODE_POOL_OSL'],
        u'by_node_pool': True
}
