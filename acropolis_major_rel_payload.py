#NUTEST_BRANCH = u'euphrates-5.16-stable'
#AOS_REL_BRANCH = u'euphrates-5.16-stable'
#PC_REL_BRANCH = u'euphrates-5.16-stable'
#OBELIX_BRANCH = u'dogmatix'


#NUTEST_BRANCH = u'euphrates-5.17-stable'
#AOS_REL_BRANCH = u'euphrates-5.17-stable'
#PC_REL_BRANCH = u'euphrates-5.17-stable'
#OBELIX_BRANCH = u'dogmatix_5.17'


NUTEST_BRANCH = u'euphrates-5.19-stable'
AOS_REL_BRANCH = u'euphrates-5.19.1-stable'
PC_REL_BRANCH = u'euphrates-5.19-stable-pc-1'
OBELIX_BRANCH = u'dogmatix_5.19'
PC_OBELIX_BRANCH = u'euphrates-5.19-stable-pc-1'


#NUTEST_BRANCH = u'master'
#AOS_REL_BRANCH = u'master'
#PC_REL_BRANCH = u'master'
#OBELIX_BRANCH = u''

#POOL_NAME = [u'AHV-REG-NODE-POOL-MASTER']
GPU_POOL_NAME = [u'ahv-gpu-regression']
POOL_NAME = [u'AHV_NODE_POOL_OSL']
SCALE_OUT_POOL_NAME = [u'acropolis_scale_Testing']


BUILD_FOLDERS = 'x86_64'
#BUILD_TYPE = 'opt'
BUILD_TYPE = 'release'

#NOS_URL = 'http://endor.dyn.nutanix.com/builds/nos-builds/euphrates-5.17-stable/07f10975017ffb710d01592cfb76fe2be5a7c74b/opt/tar/nutanix_installer_package-opt-euphrates-5.17-stable-07f10975017ffb710d01592cfb76fe2be5a7c74b.tar.gz'
NOS_URL = ''

GOS_PATCH_5_11 = u'https://gerrit.eng.nutanix.com/changes/335149/revisions/2f6eaa7d73e63b7d7ef00f61fe2e0fcabc512ff1/patch?zip'
GOS_PATCH_5_16 = u'https://gerrit.eng.nutanix.com/changes/334611/revisions/c32be2d1698fd1a9392cc3e041aaa0a38355bdbc/patch?zip'
GOS_AND_SKIP_ISSUE_5_16_PATCH = u'https://gerrit.eng.nutanix.com/changes/354886/revisions/1f68dd61b8b4d0a687eda8666985536dc66469a6/patch?zip'
GOS_PATCH_5_17 = u'https://gerrit.eng.nutanix.com/changes/359519/revisions/dd09338bb1f8bd616a8ed63d94df6447e0ed7c92/patch?zip'
GOS_PATCH_URL = GOS_PATCH_5_17



FOUNDATION_BUILD_URL = ''
#FOUNDATION_BUILD_URL = u'http://endor.dyn.nutanix.com/builds/foundation-builds/4.5/foundation-4.5-90-88e38e12-universal-release.x86_64.tar.gz'

HYPERVISOR_URL = ''
#HYPERVISOR_URL = u'http://endor.dyn.nutanix.com/builds/ahv-builds/20190308.101176/iso/AHV-DVD-x86_64-el7.nutanix.20190308.101176.iso'


PC_URL = u'http://endor.dyn.nutanix.com/builds/PC-builds/' + PC_REL_BRANCH + '/'
PC_COMMIT_ID = 'd16f9f491e077eb8f1d7382ed37ebc8cb736513d'

NOS_COMMIT_ID = '20bdb87735f6e7cd227572085854461932b7af6c'


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


ACROPOLIS_PAYLOAD_MAJOR_REL = dict()
# ACROPOLIS_PAYLOAD_MAJOR_REL['tester_tags'] = [u'all', u'v3.1', u'max_deployments__30', u'phx1',
#                                               u'sched__phx1', u'rdm__phx1', u'sched__beta',
#                                               u'official']

ACROPOLIS_PAYLOAD_MAJOR_REL['tester_tags'] = [u'v3.1', u'official']

##### Specify Nutest Branch
ACROPOLIS_PAYLOAD_MAJOR_REL['nutest_branch'] = NUTEST_BRANCH
ACROPOLIS_PAYLOAD_MAJOR_REL['test_framework'] = u'nutest'
ACROPOLIS_PAYLOAD_MAJOR_REL[u'emails'] = [u'velurusruthi.naidu@nutanix.com',
                                          u'bhawani.singh@nutanix.com', u'ritopa.dey@nutanix.com']


#ACROPOLIS_PAYLOAD_MAJOR_REL[u'emails'] = [u'acropolis-catalog@nutanix.com']


ACROPOLIS_PAYLOAD_MAJOR_REL['plugins'] = {u'post_run': [
        {u'args': {},
         u'description': u'Sends mail to the recipients.',
         u'stage': u'post_run',
         u'name': u'EmailPlugin'}]
}


ACROPOLIS_PAYLOAD_MAJOR_REL['patch_url'] = ''

ACROPOLIS_PAYLOAD_MAJOR_REL['scheduling_options'] = {
    u'optimize_scheduling': True,
    u'force_imaging': False,
    u'task_priority': 80,
    u'skip_resource_spec_match': False,
    u'upgrade': False,
    u'retry_imaging': 2,
    u'check_image_compatibility': True
}


ACROPOLIS_PAYLOAD_MAJOR_REL['build_selection'] = USE_NOS_BY_COMMIT_ID
#ACROPOLIS_PAYLOAD_MAJOR_REL['build_selection'] = USE_NOS_BY_SMOKE_PASSED

ACROPOLIS_PAYLOAD_MAJOR_REL['git'] = {
        u'repo': u'main',
        u'branch': AOS_REL_BRANCH
}
ACROPOLIS_PAYLOAD_MAJOR_REL['cluster_selection'] = {
        u'pool_name': POOL_NAME,
        u'by_node_pool': True
}
ACROPOLIS_PAYLOAD_MAJOR_REL[u'requested_hardware'] = {
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
        u'nos_url': NOS_URL,
        u'redundancy_factor': u'default',
        u'secondary_datacenters': {
            u'vsphere': {}
        },
        u'hypervisor_url': ''
    }
}
ACROPOLIS_PAYLOAD_MAJOR_REL['resource_manager_json'] = dict(PRISM_CENTRAL={
    u'build': {
        u'nos_build_url': PC_URL + PC_COMMIT_ID + '/' + BUILD_TYPE + '/'
    }
})
ACROPOLIS_PAYLOAD_PC_MAJOR_REL = ACROPOLIS_PAYLOAD_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_PC_MAJOR_REL['plugins'] = {u'post_run': [
        {u'args': {},
         u'description': u'Sends mail to the recipients.',
         u'stage': u'post_run',
         u'name': u'EmailPlugin'},
        {u'args': {u'branch': PC_OBELIX_BRANCH},
         u'description': u'Updates the branch info of the test result document with the info provided in args',
         u'name': u'UpdateBranchPlugin',
         u'stage': u'post_run'}
        ]}

ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL = {k: v for (k, v) in ACROPOLIS_PAYLOAD_MAJOR_REL.items() if k != 'resource_manager_json'}
ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_MAJOR_REL = ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_MAJOR_REL['plugins'] = {u'post_run': [
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
ACROPOLIS_PAYLOAD_GPU_MAJOR_REL = ACROPOLIS_PAYLOAD_PC_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_GPU_MAJOR_REL['cluster_selection'] = {
    u'pool_name': GPU_POOL_NAME,
    u'by_node_pool': True
}
ACROPOLIS_PAYLOAD_GPU_MAJOR_REL['tester_tags'] = [u'v3.1', u'max_deployments__1', u'official']


ACROPOLIS_PAYLOAD_GPU_PC_MAJOR_REL = ACROPOLIS_PAYLOAD_PC_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_GPU_PC_MAJOR_REL['tester_tags'] = [u'v3.1', u'max_deployments__4', u'official']
ACROPOLIS_PAYLOAD_GPU_PC_MAJOR_REL['cluster_selection'] = {
        u'pool_name': GPU_POOL_NAME,
        u'by_node_pool': True
}



ACROPOLIS_PAYLOAD_PC_UI_MAJOR_REL = ACROPOLIS_PAYLOAD_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_PC_UI_MAJOR_REL['resource_manager_json'] = dict(
    PRISM_CENTRAL={
    u'build': {
        u'nos_build_url': PC_URL + PC_COMMIT_ID + '/' + BUILD_TYPE + '/'
    }},
    SELENIUM_VM = {
    "software": {
        "build_url": "http://endor.dyn.nutanix.com/GoldImages/selenlium_windows_image/selenium_auto_start_win7.img"
    }
}
)

ACROPOLIS_PAYLOAD_VNUMA_MAJOR_REL = ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_VNUMA_MAJOR_REL['cluster_selection'] = {
        u'pool_name': POOL_NAME,
        u'by_node_pool': True
}

# ACROPOLIS_PAYLOAD_VNUMA_MAJOR_REL['cluster_selection'] = {
#     u'cluster_names': [u'cottonwood'],
#     u'by_names': True
# }
ACROPOLIS_PAYLOAD_LCM_SCHEDULER_HYPERVISOR_ANY = ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL.copy()
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
        u'hypervisor_url': HYPERVISOR_URL
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


ACROPOLIS_PAYLOAD_NO_PC_HA_MAJOR_REL = ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_NO_PC_HA_MAJOR_REL[u'requested_hardware'] = {
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
        u'hypervisor_url': ''
    }
}
ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL[u'requested_hardware'] = {
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
        u'hypervisor_url': ''
    }
}

ACROPOLIS_PAYLOAD_NO_PC_HA_MAJOR_REL = ACROPOLIS_PAYLOAD_PC_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_NO_PC_HA_MAJOR_REL[u'requested_hardware'] = {
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
        u'hypervisor_url': HYPERVISOR_URL
    }
}

ACROPOLIS_PAYLOAD_PC_OVA_HYPERVISOR_ANY_MAJOR_REL = ACROPOLIS_PAYLOAD_PC_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_PC_OVA_HYPERVISOR_ANY_MAJOR_REL[u'requested_hardware'] = {
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
        u'hypervisor_url': HYPERVISOR_URL
    }
}



ACROPOLIS_PAYLOAD_PC_CATALOG_MAJOR_REL = ACROPOLIS_PAYLOAD_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_PC_CATALOG_MAJOR_REL['plugins'] = {u'post_run': [
        {u'args': {},
         u'description': u'Sends mail to the recipients.',
         u'stage': u'post_run',
         u'name': u'EmailPlugin'},
        {u'args': {u'branch': PC_OBELIX_BRANCH},
         u'description': u'Updates the branch info of the test result document with the info provided in args',
         u'name': u'UpdateBranchPlugin',
         u'stage': u'post_run'}
        ]}

ACROPOLIS_PAYLOAD_PC_CATALOG_MAJOR_REL["emails"] = [u'velurusruthi.naidu@nutanix.com', u'bhawani.singh@nutanix.com',
                                                    u'acropolis-catalog@nutanix.com', u'vivekanandan.k@nutanix.com',
                                                    u'ritopa.dey@nutanix.com']

ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MAJOR_REL = ACROPOLIS_PAYLOAD_PC_CATALOG_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MAJOR_REL['tester_tags'].append(u'nutest__resources')
ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MAJOR_REL[u'requested_hardware'] = {
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
ACROPOLIS_PAYLOAD_PC_CATALOG_ESX_MAJOR_REL = ACROPOLIS_PAYLOAD_PC_CATALOG_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_PC_CATALOG_ESX_MAJOR_REL[u'requested_hardware'] = {
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

ACROPOLIS_PAYLOAD_PC_SCALEOUT_MAJOR_REL = ACROPOLIS_PAYLOAD_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_PC_SCALEOUT_MAJOR_REL['cluster_selection'] = {
        u'pool_name': SCALE_OUT_POOL_NAME,
        u'by_node_pool': True
}



ACROPOLIS_PAYLOAD_SCHEDULER_OPT_MAJOR_REL = ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_SCHEDULER_OPT_MAJOR_REL['scheduling_options'] = {
    u'optimize_scheduling': True,
    u'force_imaging': False,
    u'task_priority': 80,
    u'skip_resource_spec_match': False,
    u'upgrade': False,
    u'retry_imaging': 2,
    u'check_image_compatibility': True
}


ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MAJOR_REL = ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL.copy()
ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MAJOR_REL['tester_tags'] = [u'v3.1', u'max_deployments__1', u'official']

ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MAJOR_REL['scheduling_options'] = {
    u'optimize_scheduling': False,
    u'force_imaging': False,
    u'task_priority': 80,
    u'skip_resource_spec_match': False,
    u'upgrade': False,
    u'retry_imaging': 2,
    u'check_image_compatibility': True,
    u'class_wise_scheduling': True
}

ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MAJOR_REL['plugins'] = {u'post_run': [
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

ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MAJOR_REL['patch_url'] = GOS_PATCH_URL
#ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MASTER[u'emails'] = [u'bhawani.singh@nutanix.com']

