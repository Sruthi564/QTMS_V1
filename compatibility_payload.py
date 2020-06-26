PE_MATRIX = {
    "5.5.9": [
        {"Catalog": [{"nutest_branch": "euphrates-5.5.6-stable", "nos_branch": "euphrates-5.5.9-stable",
                      "test_set": "Regression_Acropolis_MTS_Nutest_XI_Catalog_5.5.x2",
                      "email": [u'saurabh.dohare@nutanix.com'],
                      "pool_name": [u'AHV_NODE_POOL_OSL']}]},
        {"Metropolis": [{"nutest_branch": "euphrates-5.5-stable", "nos_branch": "euphrates-5.5.9-stable",
                         "test_set": "Acropolis_MTS_Nutest_Metropolis_5.5.x",
                         "email": [u'bhawani.singh@nutanix.com'],
                         "pool_name": [u'AHV_NODE_POOL_OSL']}]}
    ],
    "5.8.2": [
        {"Catalog": [{"nutest_branch": "euphrates-5.8-stable", "nos_branch": "euphrates-5.8.2-stable",
                      "test_set": "Regression_Acropolis_MTS_Nutest_XI_Catalog_5.8.x",
                      "email": [u'saurabh.dohare@nutanix.com'],
                      "pool_name": [u'AHV_NODE_POOL_OSL']}]},
        {"Metropolis": [{"nutest_branch": "euphrates-5.8-stable", "nos_branch": "euphrates-5.8.2-stable",
                         "test_set": "Acropolis_MTS_Nutest_Metropolis_5.8.x",
                         "email": [u'bhawani.singh@nutanix.com'],
                         "pool_name": [u'AHV_NODE_POOL_OSL']}]}
    ],
    "5.9.2": [
        {"Catalog": [{"nutest_branch": "euphrates-5.9-stable", "nos_branch": "euphrates-5.9.2-stable",
                     "test_set": "Regression_Acropolis_MTS_Nutest_XI_Catalog_5.9.x",
                      "email": [u'saurabh.dohare@nutanix.com'],
                      "pool_name": [u'AHV_NODE_POOL_OSL']}]},
        {"Metropolis": [{"nutest_branch": "euphrates-5.9-stable", "nos_branch": "euphrates-5.9.2-stable",
                         "test_set": "Acropolis_MTS_Nutest_Metropolis_5.9.x",
                         "email": [u'bhawani.singh@nutanix.com'],
                         "pool_name": [u'AHV_NODE_POOL_OSL']}]}
    ],
    "5.10.2": [
        {"Catalog": [{"nutest_branch": "euphrates-5.10-stable", "nos_branch": "euphrates-5.10.2-stable",
                      "test_set": "Regression_Acropolis_MTS_Nutest_XI_Catalog_Master",
                      "email": [u'saurabh.dohare@nutanix.com'],
                      "pool_name": [u'AHV_NODE_POOL_OSL']}]},
        {"Metropolis": [{"nutest_branch": "euphrates-5.10-stable", "nos_branch": "euphrates-5.10.2-stable",
                         "test_set": "Acropolis_MTS_Nutest_Metropolis_master",
                         "email": [u'bhawani.singh@nutanix.com'],
                         "pool_name": [u'AHV_NODE_POOL_OSL']}]}
    ],
    "5.10.4": [
        {"Catalog": [{"nutest_branch": "euphrates-5.10-stable", "nos_branch": "euphrates-5.10.4-stable",
                      "test_set": "Regression_Acropolis_MTS_Nutest_XI_Catalog_Master",
                      "email": [u'saurabh.dohare@nutanix.com'],
                      "pool_name": [u'AHV_NODE_POOL_OSL']}]},
        {"Metropolis": [{"nutest_branch": "euphrates-5.10-stable", "nos_branch": "euphrates-5.10.4-stable",
                         "test_set": "Acropolis_MTS_Nutest_Metropolis_master",
                         "email": [u'bhawani.singh@nutanix.com'],
                         "pool_name": [u'AHV_NODE_POOL_OSL']}]}
    ],
    "5.10.5": [
        {"Catalog": [{"nutest_branch": "euphrates-5.10-stable", "nos_branch": "euphrates-5.10.5-stable",
                      "test_set": "Regression_Acropolis_MTS_Nutest_XI_Catalog_Master",
                      "email": [u'saurabh.dohare@nutanix.com'],
                      "pool_name": [u'AHV_NODE_POOL_OSL']}]},
        {"Metropolis": [{"nutest_branch": "euphrates-5.10-stable", "nos_branch": "euphrates-5.10.5-stable",
                         "test_set": "Acropolis_MTS_Nutest_Metropolis_master",
                         "email": [u'bhawani.singh@nutanix.com'],
                         "pool_name": [u'AHV_NODE_POOL_OSL']}]}
    ]
}


PC_MATRIX = {
    "5.10.2": [
        {"commit_id": "42b116301be8a3547b5e863b506185bc6db89478", "branch": u'euphrates-5.10.2-stable'}
    ],
    "5.9.2": [
        {"commit_id": None, "branch": u'euphrates-5.9.2-stable'}
    ],
    "5.10.3": [
        {"commit_id": "b73a7a0ab89dd9c1ea0d2dfbc9570d545058a45e", "branch": u'euphrates-5.10.3-stable'}
    ],
    "5.10.4": [
        {"commit_id": "58b84348b404a6245a612bc12b4265e34c337426", "branch": u'euphrates-5.10.4-stable'}
    ],
    "5.10.5": [
        {"commit_id": "0af34835c53f380d0ea6a0d4e321e514d43c02e3", "branch": u'euphrates-5.10.5-stable'}
    ],
    "5.11": [
        {"commit_id": "8032e8a5afc05b1df72f03267f9269b3f8d32209", "branch": u'euphrates-5.11-stable'}
    ]
}

SAMPLE_COMPATIBILITY_PAYLOAD = {
    u'last_triggered': {
        u'$date': 1546086188866},
    u'updated_at': {
        u'$date': 1546086188867},
    u'private': False,
    u'created_by': u'5b1a20031b54d09bbe61f424',
    u'plugins': {
        u'post_run': [{
            u'args': {},
            u'description': u'Performs Auto triaging based upon the test failure.',
            u'stage': u'post_run', u'name': u'AutoTriageHistory'}, {
            u'args': {},
            u'description': u'Sends mail to the recipients.',
            u'name': u'EmailPlugin', u'stage': u'post_run'}
        ],
        u'pre_run': []},
    u'test_source_repo': u'nutest',
    u'auto_schedule_cron': False,
    u'build_selection': {
        u'use_stable_nutest_commit': False,
        u'by_latest_smoked': True,
        u'build_type': u'opt',
        u'use_stable_agave_commit': False},
    u'git': {
        u'repo': u'main',
        u'branch': u'euphrates-5.5.8-stable'},
    u'service': u'PC',
    u'image_branch': u'',
    u'skip_commit_id_validation': False,
    u'image_build_type': u'None',
    u'test_sets': [{
        u'$oid': u'5b3a2abc1b54d0c59868f570'}],
    u'cluster_selection': {
        u'pool_name': [
            u'Acropolis'],
        u'by_node_pool': True},
    u'requested_hardware': {
        u'hypervisor_version': u'branch_symlink',
        u'hypervisor': u'kvm',
        u'imaging_options': {
            u'datacenter': {
                u'hyperv': {},
                u'kvm': {},
                u'vsphere': {},
                u'use_host_names': False},
            u'min_ram': u'15',
            u'redundancy_factor': u'default',
            u'secondary_datacenters': {
                u'vsphere': {}}}},
    u'description': u'Compatibility_Acropolis_MTS_Nutest_XI_Catalog_5.10.1_5.5.8_5.10',
    u'image_commit': u'',
    u'nutest_branch': u'euphrates-5.10-stable',
    u'test_framework': u'nutest',
    u'tester_tags': [
        u'v3.1',
        u'max_deployments__30'],
    u'skip_bad_tests': False,
    u'image_build_selection': u'By Commit',
    u'emails': [u'saurabh.dohare@nutanix.com'],
    u'scheduled_jobs': [{
        u'$oid': u'5ba33f21114cdb49f5c02ae9'}, {
        u'$oid': u'5bb9d33e114cdb10526353c9'}, {u'$oid': u'5bc4270d114cdb495c6953fa'}, {u'$oid': u'5bd01ce8114cdbee60436d59'}, {u'$oid': u'5bee69e6114cdb48ee0098ae'}, {u'$oid': u'5bf658a2114cdb7a936b6df3'}, {u'$oid': u'5bfd0cdd114cdbba6f89dc2b'}, {u'$oid': u'5c010cc9114cdbd87da7fc70'}, {u'$oid': u'5c27672a114cdbd2238e8d39'}
    ],
    u'name': u'Compatibility_Acropolis_MTS_Nutest_XI_Catalog_5.10.1_5.5.8_5.10',
    u'scheduling_options': {
        u'optimize_scheduling': True,
        u'force_imaging': False,
        u'task_priority': 10,
        u'skip_resource_spec_match': False,
        u'upgrade': False,
        u'retry_imaging': 0,
        u'check_image_compatibility': True},
    u'created_at': {
        u'$date': 1537425123041},
    u'package_type': u'tar',
    u'resource_manager_json': {
        u'PRISM_CENTRAL': {u'build': {u'nos_build_url': u'http://10.40.64.33/builds/pc-builds/euphrates-5.10.1-stable/latest/opt/'}}},
    u'created_by_user': {u'$oid': u'5b1a20031b54d09bbe61f424'}, u'demo_mode': False, u'v': 3, u'_id': {u'$oid': u'5ba33ee3114cdb6402394fb0'}}



NEW_COMPATIBILITY_PAYLOAD = {
    u'private': False,
    u'plugins': {
        u'post_run': [
            {
                u'args': {}, u'description': u'Sends mail to the recipients.',
                u'name': u'EmailPlugin', u'stage': u'post_run'}
        ],
        u'pre_run': []},
    u'test_source_repo': u'nutest',
    u'auto_schedule_cron': False,
    u'build_selection': {
        u'use_stable_nutest_commit': False,
        u'by_latest_smoked': True,
        u'build_type': u'opt',
        u'use_stable_agave_commit': False},
    u'git': {
        u'repo': u'main',
        u'branch': ''},
    u'service': u'PC',
    u'image_branch': u'',
    u'skip_commit_id_validation': False,
    u'image_build_type': u'None',
    u'test_sets': [{
        u'$oid': ''}],
    u'cluster_selection': {
        u'pool_name': [''],
        u'by_node_pool': True},
    u'requested_hardware': {
        u'hypervisor_version': u'branch_symlink',
        u'hypervisor': u'kvm',
        u'imaging_options': {
            u'datacenter': {
                u'hyperv': {},
                u'kvm': {},
                u'vsphere': {},
                u'use_host_names': False},
            u'redundancy_factor': u'default',
            u'secondary_datacenters': {
                u'vsphere': {}}}},
    u'description': u'Compatibility_Acropolis_MTS_Nutest_',
    u'image_commit': '',
    u'nutest_branch': '',
    u'test_framework': u'nutest',
    u'tester_tags': [
        u'nutest',
        u'v3.1',
        u'max_deployments__30',
        u'phx1',
        u'sched__phx1',
        u'rdm__phx1'],
    u'skip_bad_tests': False,
    u'emails': [],
    u'name': u'Compatibility_Acropolis_MTS_Nutest_',
    u'scheduling_options': {
        u'optimize_scheduling': True,
        u'force_imaging': False,
        u'task_priority': 80,
        u'skip_resource_spec_match': False,
        u'upgrade': False,
        u'retry_imaging': 0,
        u'check_image_compatibility': True},
    u'package_type': u'tar',
    u'resource_manager_json': {
        u'PRISM_CENTRAL': {
            u'build': {
                u'nos_build_url': ''}}},
    u'demo_mode': False,
    u'v': 3
}
