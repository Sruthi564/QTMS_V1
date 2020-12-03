
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
#AOS_REL_BRANCH = u'euphrates-5.10.8-stable'
#PC_REL_BRANCH = u'euphrates-5.10.8-stable'
#OBELIX_BRANCH = u'obelix_5.10.8'

#NUTEST_BRANCH = u'euphrates-5.11-stable'
#AOS_REL_BRANCH = u'euphrates-5.11.2-stable'
#PC_REL_BRANCH = u'euphrates-5.11.2-stable'
#OBELIX_BRANCH = u'obelix_5.11.1'

#NUTEST_BRANCH = u'euphrates-5.15-stable'
#AOS_REL_BRANCH = u'euphrates-5.15-stable'
#PC_REL_BRANCH = u'euphrates-5.11.3-stable'
#OBELIX_BRANCH = u'obelix'


NUTEST_BRANCH = u'euphrates-5.19-stable'
AOS_REL_BRANCH = u'euphrates-5.15.4-stable'
PC_REL_BRANCH = u'euphrates-5.19-stable-pc-0'
OBELIX_BRANCH = u'obelix_5.15'


#NUTEST_BRANCH = u'euphrates-5.15-stable'
#AOS_REL_BRANCH = u'euphrates-5.15.2-stable'
#PC_REL_BRANCH = u'euphrates-5.15.2-stable'
#OBELIX_BRANCH = u'obelix'


#NUTEST_BRANCH = u'euphrates-5.17-stable'
#AOS_REL_BRANCH = u'euphrates-5.17.1-stable'
#PC_REL_BRANCH = u'euphrates-5.17.1-stable'
#OBELIX_BRANCH = u'dogmatix_5.17'



#NUTEST_BRANCH = u'euphrates-5.16-stable'
#AOS_REL_BRANCH = u'euphrates-5.16.1-stable'
#PC_REL_BRANCH = u'euphrates-5.16.1-stable'
#OBELIX_BRANCH = u'dogmatix'

#POOL_NAME = [u'AHV-REG-NODE-POOL-MASTER']
GPU_POOL_NAME = [u'ahv-gpu-regression']
POOL_NAME = [u'AHV_NODE_POOL_OSL']


BUILD_FOLDERS = 'x86_64'
#BUILD_TYPE = 'opt'
BUILD_TYPE = 'release'

NOS_URL = ''

HYPERVISOR_BUILD_URL = ''

#HYPERVISOR_BUILD_URL = 'http://endor.dyn.nutanix.com/builds/ahv-builds/20190916.231/iso/AHV-DVD-x86_64-el7.nutanix.20190916.231.iso'

#NOS_URL = 'http://endor.dyn.nutanix.com/releases/Euphrates-5.15-stable-RC1/f322bb1e20845aadc476b89eaf0647397e8a3222/x86_64/opt/tar/nutanix_installer_package-opt-euphrates-5.15-stable-f322bb1e20845aadc476b89eaf0647397e8a3222-x86_64.tar.gz'


FOUNDATION_BUILD_URL = ''
#FOUNDATION_BUILD_URL = u'http://endor.dyn.nutanix.com/builds/foundation-builds/4.5/foundation-4.5-90-88e38e12-universal-release.x86_64.tar.gz'

PC_URL = u'http://endor.dyn.nutanix.com/builds/PC-builds/' + PC_REL_BRANCH + '/'


PC_COMMIT_ID = '37074216edfb0d13269874c8dffb7a0aa68fd314'

NOS_COMMIT_ID = '3218a31e15584e368dc4c9b7abc4d99da585c8d2'


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


ACROPOLIS_PAYLOAD_MINOR_REL = dict()
# ACROPOLIS_PAYLOAD_MINOR_REL['tester_tags'] = [u'all', u'v3.1', u'max_deployments__30', u'phx1',
#                                               u'sched__phx1', u'rdm__phx1', u'sched__beta',
#                                               u'official']

ACROPOLIS_PAYLOAD_MINOR_REL['tester_tags'] = [u'v3.1', u'max_deployments__7', u'official']
#ACROPOLIS_PAYLOAD_MINOR_REL['tester_tags'] = [u'v3.1', u'max_deployments__7']


##### Specify Nutest Branch
ACROPOLIS_PAYLOAD_MINOR_REL['nutest_branch'] = NUTEST_BRANCH
ACROPOLIS_PAYLOAD_MINOR_REL['test_framework'] = u'nutest'
ACROPOLIS_PAYLOAD_MINOR_REL[u'emails'] = [u'velurusruthi.naidu@nutanix.com', u'bhawani.singh@nutanix.com']

ACROPOLIS_PAYLOAD_MINOR_REL['plugins'] = {u'post_run': [
        {u'args': {},
         u'description': u'Sends mail to the recipients.',
         u'stage': u'post_run',
         u'name': u'EmailPlugin'}]
}


ACROPOLIS_PAYLOAD_MINOR_REL['patch_url'] = ''

ACROPOLIS_PAYLOAD_MINOR_REL['scheduling_options'] = {
    u'optimize_scheduling': True,
    u'force_imaging': False,
    u'task_priority': 80,
    u'skip_resource_spec_match': False,
    u'upgrade': False,
    u'retry_imaging': 2,
    u'check_image_compatibility': True
}


ACROPOLIS_PAYLOAD_MINOR_REL['build_selection'] = USE_NOS_BY_COMMIT_ID
#ACROPOLIS_PAYLOAD_MINOR_REL['build_selection'] = USE_NOS_BY_SMOKE_PASSED

ACROPOLIS_PAYLOAD_MINOR_REL['git'] = {
        u'repo': u'main',
        u'branch': AOS_REL_BRANCH
}
ACROPOLIS_PAYLOAD_MINOR_REL['cluster_selection'] = {
        u'pool_name': POOL_NAME,
        u'by_node_pool': True
}
### Around line 130-148
ACROPOLIS_PAYLOAD_MINOR_REL[u'requested_hardware'] = {
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
ACROPOLIS_PAYLOAD_MINOR_REL['resource_manager_json'] = dict(PRISM_CENTRAL={
    u'build': {
        u'nos_build_url': PC_URL + PC_COMMIT_ID + '/' + BUILD_TYPE + '/'
    }
})
ACROPOLIS_PAYLOAD_PC_MINOR_REL = ACROPOLIS_PAYLOAD_MINOR_REL
ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL = {k: v for (k, v) in ACROPOLIS_PAYLOAD_MINOR_REL.items() if k != 'resource_manager_json'}
ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_MINOR_REL = ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL.copy()
ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_MINOR_REL['plugins'] = {u'post_run': [
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
ACROPOLIS_PAYLOAD_GPU_MINOR_REL = ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL.copy()
ACROPOLIS_PAYLOAD_GPU_MINOR_REL['cluster_selection'] = {
    u'pool_name': GPU_POOL_NAME,
    u'by_node_pool': True
}
ACROPOLIS_PAYLOAD_GPU_MINOR_REL['tester_tags'] = [u'v3.1', u'max_deployments__1', u'official']
#ACROPOLIS_PAYLOAD_GPU_MINOR_REL['tester_tags'] = [u'v3.1', u'max_deployments__1']

ACROPOLIS_PAYLOAD_VNUMA_MINOR_REL = ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL.copy()
ACROPOLIS_PAYLOAD_VNUMA_MINOR_REL['cluster_selection'] = {
        u'pool_name': POOL_NAME,
        u'by_node_pool': True
}


# ACROPOLIS_PAYLOAD_VNUMA_MINOR_REL['cluster_selection'] = {
#     u'cluster_names': [u'cottonwood'],
#     u'by_names': True
# }
ACROPOLIS_PAYLOAD_LCM_SCHEDULER_HYPERVISOR_ANY = ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL.copy()
ACROPOLIS_PAYLOAD_LCM_SCHEDULER_HYPERVISOR_ANY[u'requested_hardware'] = {
    u'hypervisor_version': None,
    u'hypervisor': None,
    u'imaging_options': {
        u'datacenter': {
            u'hyperv': {},
            u'kvm': {},
            u'vsphere': {},
            u'use_host_names': False
        },
        u'foundation_build_url': FOUNDATION_BUILD_URL,
        u'min_ram': u'15',
        u'nos_url': NOS_URL,
        u'redundancy_factor': u'default',
        u'secondary_datacenters': {
            u'vsphere': {}
        },
        u'hypervisor_url': ''
    }
}
ACROPOLIS_PAYLOAD_LCM_SCHEDULER_HYPERVISOR_ANY['scheduling_options'] = {
    u'optimize_scheduling': True,
    u'force_imaging': True,
    u'task_priority': 80,
    u'skip_resource_spec_match': False,
    u'upgrade': False,
    u'retry_imaging': 0,
    u'check_image_compatibility': True,

}


ACROPOLIS_PAYLOAD_NO_PC_HA_MINOR_REL = ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL.copy()
ACROPOLIS_PAYLOAD_NO_PC_HA_MINOR_REL[u'requested_hardware'] = {
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
        u'nos_url': NOS_URL,
        u'redundancy_factor': u'3',
        u'secondary_datacenters': {
            u'vsphere': {}
        },
        u'hypervisor_url': HYPERVISOR_BUILD_URL
    }
}
ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL[u'requested_hardware'] = {
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
        u'nos_url': NOS_URL,
        u'redundancy_factor': u'default',
        u'secondary_datacenters': {
            u'vsphere': {}
        },
        u'hypervisor_url': HYPERVISOR_BUILD_URL
    }
}
ACROPOLIS_PAYLOAD_PC_CATALOG_MINOR = ACROPOLIS_PAYLOAD_MINOR_REL.copy()
ACROPOLIS_PAYLOAD_PC_CATALOG_MINOR["emails"] = [u'velurusruthi.naidu@nutanix.com', u'bhawani.singh@nutanix.com',
                                                u'acropolis-catalog@nutanix.com', u'vivekanandan.k@nutanix.com']
ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MINOR = ACROPOLIS_PAYLOAD_PC_CATALOG_MINOR.copy()
ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MINOR['tester_tags'] = [u'v3.1', u'max_deployments__7', u'official', u'nutest__resources']
ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MINOR[u'requested_hardware'] = {
    u'hypervisor_version': u'branch_symlink',
    u'hypervisor': None,
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
ACROPOLIS_PAYLOAD_PC_CATALOG_ESX_MINOR = ACROPOLIS_PAYLOAD_PC_CATALOG_MINOR.copy()
ACROPOLIS_PAYLOAD_PC_CATALOG_ESX_MINOR[u'requested_hardware'] = {
    u'hypervisor_version': None,
    u'hypervisor': None,
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
ACROPOLIS_PAYLOAD_SCHEDULER_OPT_MINOR_REL = ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL.copy()
ACROPOLIS_PAYLOAD_SCHEDULER_OPT_MINOR_REL['scheduling_options'] = {
    u'optimize_scheduling': True,
    u'force_imaging': False,
    u'task_priority': 80,
    u'skip_resource_spec_match': False,
    u'upgrade': False,
    u'retry_imaging': 2,
    u'check_image_compatibility': True
}


ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MINOR_REL = ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL.copy()
ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MINOR_REL['tester_tags'] = [u'v3.1', u'max_deployments__1', u'official']
#ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MINOR_REL['tester_tags'] = [u'v3.1', u'max_deployments__1']

ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MINOR_REL['scheduling_options'] = {
    u'optimize_scheduling': False,
    u'force_imaging': False,
    u'task_priority': 80,
    u'skip_resource_spec_match': False,
    u'upgrade': False,
    u'retry_imaging': 2,
    u'check_image_compatibility': True,
    u'class_wise_scheduling': True
}
ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MINOR_REL['plugins'] = {u'post_run': [
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
ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MINOR_REL['patch_url'] = u'https://gerrit.eng.nutanix.com/changes/335149/revisions/2f6eaa7d73e63b7d7ef00f61fe2e0fcabc512ff1/patch?zip'
#ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MASTER[u'emails'] = [u'bhawani.singh@nutanix.com']



