from qtms import QTMS
from job_profile import *
from acropolis_master_payload import *
from uhura_master_payload import UHURA_PAYLOAD_PC_MASTER, UHURA_PAYLOAD_NO_PC_NO_VC_MASTER, \
    UHURA_PAYLOAD_NO_PC_WITH_VC_MASTER, UHURA_PAYLOAD_NS_WITH_VC_MASTER, UHURA_PAYLOAD_NS_NO_VC_MASTER
from gold_suite_payload import GOLD_SUITE_PAYLOAD_PC, GOLD_SUITE_PAYLOAD_NO_PC, GOLD_SUITE_PAYLOAD_GPU, \
    GOLD_SUITE_PAYLOAD_UHURA
from acropolis_payload_lts import ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_LTS, ACROPOLIS_PAYLOAD_NO_PC_LTS, \
    ACROPOLIS_PAYLOAD_GPU_LTS, ACROPOLIS_PAYLOAD_VNUMA_LTS, ACROPOLIS_PAYLOAD_NO_PC_HA_LTS
from uhura_payload_lts import UHURA_PAYLOAD_NO_PC_WITH_VC_LTS, UHURA_PAYLOAD_NO_PC_NO_VC_LTS, \
    UHURA_PAYLOAD_NS_NO_VC_LTS, UHURA_PAYLOAD_NS_WITH_VC_LTS
from uhura_major_rel_payload import UHURA_PAYLOAD_NO_PC_WITH_VC_MAJOR_REL, UHURA_PAYLOAD_NO_PC_NO_VC_MAJOR_REL, \
    UHURA_PAYLOAD_PC_MAJOR_REL, UHURA_PAYLOAD_NS_WITH_VC_MAJOR_REL, UHURA_PAYLOAD_NS_NO_VC_MAJOR_REL
from acropolis_major_rel_payload import *
from acropolis_minor_rel_payload import *
from uhura_minor_rel_payload import *

CATALOG_EMAIL_LIST = [u'alejand.mier@nutanix.com', u'mohammad.parvez@nutanix.com', u'chaitanya.karlekar@nutanix.com',
                      u'guillermo.zapatamond@nutanix.com', u'mladen.drobnjakovic@nutanix.com', u'mohammed@nutanix.com',
                      u'saurabh.dohare@nutanix.com', u'shashank.kumar@nutanix.com', u'suraj.kasi@nutanix.com',
                      u'vivekanandan.k@nutanix.com']

class Factory(object):

    def factory(class_type):
        if class_type == 'AcropolisMaster': return AcropolisMaster()
        if class_type == 'AcropolisMasterNonRegHandedover': return AcropolisMasterNonRegHandedover()
        if class_type == 'AcropolisMinor' : return AcropolisMinor()
        if class_type == 'UhuraMaster': return UhuraMaster()
        if class_type == 'AcropolisMajor': return AcropolisMajor()
        if class_type == 'UhuraMajor': return UhuraMajor()
        if class_type == 'UhuraMinor': return UhuraMinor()
        if class_type == 'AcropolisMR': return AcropolisMR()
        if class_type == 'UhuraMR': return UhuraMR()
        if class_type == 'AHVGoldSuitePatch': return AHVGoldSuitePatch()
        if class_type == 'AHVCompatibilityTest': return AHVCompatibilityTest()
        assert 0, "Bad Class Type: "+class_type
    factory = staticmethod(factory)


class QTMSRunner(object):

    def __init__(self, release_classes, operations):
        self.rel_classes = release_classes
        self.qtms_operations = operations
        self.rel_class_objects = [Factory.factory(class_type) for class_type in self.rel_classes]

    def qtms_run(self):
        for qtms_operation in self.qtms_operations:
            if qtms_operation == 'rel_sp_operations':
                for rel_class_object in self.rel_class_objects:
                    rel_class_object.execute_qtms_ops()
            if qtms_operation == 'kill_jita_tasks':
                pass
            if qtms_operation == 'get_node_pool_utilization':
                pass


class AcropolisMaster(QTMS):

    def __init__(self):
        QTMS.__init__(self)
        self.jita_operations = [
     {"op": 'update_job_profile'},
     #{"op": 'trigger_job_profile'}
        ]
        self.job_profiles = []
        self.catalog_job_profiles = []
        self.reg_handedover_job_profiles = []
        self.non_reg_handedover_job_profiles = []

        self.archived_job_profiles = [
            # #{"jps": ACROPOLIS_JPS_MASTER["PC-NO-CLONE"], "payload": ACROPOLIS_PAYLOAD_PC_NO_CLONE_MASTER}, // To be removed from Regression Suite.
            # #{"jps": ACROPOLIS_JPS_MASTER["NO-PC-HA"], "payload": ACROPOLIS_PAYLOAD_NO_PC_HA_MASTER}, // To be removed from Regression Suite.
            # #{"jps": ACROPOLIS_JPS_MASTER["PC-OVA"], "payload": ACROPOLIS_PAYLOAD_PC_OVA_HYPERVISOR_ANY}, // To be removed from Regression Suite.
            # #{"JP_NAME": "Regression_Acropolis_MTS_Nutest_Scheduler_Defrag_master", "max_dep": [u'max_deployments__1'], "sub-component": "storage-persona", "category": 'reg-handedover', "JP_ID": "5d80f14f7b48b11e4c1490e5", "FQA": ["dipika.darshan@nutanix.com"]} // Removed as they are unstable
        ]

        self.catalog_job_profiles = [
            {"jps": ACROPOLIS_JPS_MASTER["PC-CATALOG"], "payload": ACROPOLIS_PAYLOAD_PC_MASTER, "emails": CATALOG_EMAIL_LIST},
            {"jps": ACROPOLIS_JPS_MASTER["PC-CATALOG-HYPERVISOR-ANY"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MASTER, "emails": CATALOG_EMAIL_LIST},
            {"jps": ACROPOLIS_JPS_MASTER["PC-CATALOG-ESX"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_ESX_MASTER, "emails": CATALOG_EMAIL_LIST},
            {"jps": ACROPOLIS_JPS_MASTER["PE-CATALOG"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MASTER, "emails": CATALOG_EMAIL_LIST},
        ]

        self.reg_handedover_job_profiles = [
           {"jps": ACROPOLIS_JPS_MASTER["PC"], "payload": ACROPOLIS_PAYLOAD_PC_MASTER, "emails": None},

           {"jps": ACROPOLIS_JPS_MASTER["GUEST-OS-OTHERS"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MASTER, "emails": None},
           {"jps": ACROPOLIS_JPS_MASTER["NO-PC"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MASTER, "emails": None},
           {"jps": ACROPOLIS_JPS_MASTER["GPU"], "payload": ACROPOLIS_PAYLOAD_GPU_MASTER, "emails": None},
           {"jps": ACROPOLIS_JPS_MASTER["VNUMA"], "payload": ACROPOLIS_PAYLOAD_VNUMA_MASTER, "emails": None},


            #####nested###{"jps": ACROPOLIS_JPS_MASTER["GUEST-OS-OPT"], "payload": ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MASTER, "emails": None},
            {"jps": ACROPOLIS_JPS_MASTER["SCHEDULER-UPGRADES-LCM"], "payload": ACROPOLIS_PAYLOAD_LCM_SCHEDULER_HYPERVISOR_ANY, "emails": None},

            {"jps": ACROPOLIS_JPS_MASTER["SCHEDULER-OPT"], "payload": ACROPOLIS_PAYLOAD_SCHEDULER_OPT_MASTER, "emails": None},
            {"jps": ACROPOLIS_JPS_MASTER["NO-PC-HA"], "payload": ACROPOLIS_PAYLOAD_NO_PC_HA_MASTER, "emails": None},

        ]
        self.non_reg_handedover_job_profiles = [
            {"jps": ACROPOLIS_JPS_NON_REG_HANDEDOVER["PC"], "payload": ACROPOLIS_PAYLOAD_PC_MASTER, "emails": None},
            {"jps": ACROPOLIS_JPS_NON_REG_HANDEDOVER["PC-OVA"], "payload": ACROPOLIS_PAYLOAD_PC_OVA_HYPERVISOR_ANY, "emails": None},
            {"jps": ACROPOLIS_JPS_NON_REG_HANDEDOVER["PC-SCALEOUT"], "payload": ACROPOLIS_PAYLOAD_PC_SCALEOUT_MASTER, "emails": None},

        ]

        self.job_profiles.extend(self.catalog_job_profiles)
        #self.job_profiles.extend(self.reg_handedover_job_profiles)
        #self.job_profiles.extend(self.non_reg_handedover_job_profiles)


class AcropolisMasterNonRegHandedover(QTMS):

    def __init__(self):
        QTMS.__init__(self)
        self.jita_operations = [
#            {"op": 'update_job_profile'},
#            {"op": 'trigger_job_profile'}
        ]
        self.job_profiles = [
            # {"jps": ACROPOLIS_JPS_NON_REG_HANDEDOVER["PC"], "payload": ACROPOLIS_PAYLOAD_PC_MASTER, "emails": None},
            # {"jps": ACROPOLIS_JPS_NON_REG_HANDEDOVER["PC-OVA"], "payload": ACROPOLIS_PAYLOAD_PC_OVA_HYPERVISOR_ANY, "emails": None},
             #{"jps": ACROPOLIS_JPS_NON_REG_HANDEDOVER["NO-PC"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MASTER, "emails": None},
            #{"jps": ACROPOLIS_JPS_MASTER["GPU"], "payload": ACROPOLIS_PAYLOAD_GPU_MASTER, "emails": None}
        ]


class AcropolisMajor(QTMS):

    def __init__(self):
        QTMS.__init__(self)
        self.jita_operations = [
      {"op": 'clone_job_profile', "fromBranch": 'master', "toBranch": '5.18'},
      #{"op": 'update_job_profile'},
      #{"op": 'trigger_job_profile'}
         ]

        self.clone_from_jps = []
        self.clone_from_master_jps = []
        self.clone_from_major_jps = []


        clone_from_flag = "master"
        # clone_from_flag = "major"


        self.clone_from_master_jps = [
          #{"jps": ACROPOLIS_JPS_MASTER["PC-CATALOG"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_MAJOR_REL, "jp_type": "PC-CATALOG", "emails": CATALOG_EMAIL_LIST},
          #{"jps": ACROPOLIS_JPS_MASTER["PC-CATALOG-HYPERVISOR-ANY"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MAJOR_REL, "jp_type": "PC-CATALOG-HYPERVISOR-ANY", "emails": CATALOG_EMAIL_LIST},
          #{ "jps": ACROPOLIS_JPS_MASTER["PC-CATALOG-ESX"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_ESX_MASTER, "jp_type": "PC-CATALOG-ESX", "emails": CATALOG_EMAIL_LIST},
          #{"jps": ACROPOLIS_JPS_MASTER["PE-CATALOG"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL, "jp_type": "PE-CATALOG", "emails": CATALOG_EMAIL_LIST},

          #{"jps": ACROPOLIS_JPS_MASTER["PC"], "payload": ACROPOLIS_PAYLOAD_PC_MAJOR_REL, "jp_type": "PC", "emails": None},
          #{"jps": ACROPOLIS_JPS_MASTER["GUEST-OS-OTHERS"], "payload": ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_MAJOR_REL, "jp_type": "GUEST-OS-OTHERS", "emails": None},
          #{"jps": ACROPOLIS_JPS_MASTER["NO-PC"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL, "jp_type": "NO-PC", "emails": None},
          #{"jps": ACROPOLIS_JPS_MASTER["GPU"], "payload": ACROPOLIS_PAYLOAD_GPU_MAJOR_REL, "jp_type": "GPU", "emails": None},
          #{"jps": ACROPOLIS_JPS_MASTER["VNUMA"], "payload": ACROPOLIS_PAYLOAD_VNUMA_MAJOR_REL, "jp_type": "VNUMA", "emails": None},
          #{"jps": ACROPOLIS_JPS_MASTER["Xi-MGMT"], "payload": ACROPOLIS_PAYLOAD_PC_MAJOR_REL, "jp_type": "Xi-MGMT", "emails": None},

          #{"jps": ACROPOLIS_JPS_MASTER["GUEST-OS-OPT"], "payload": ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MAJOR_REL, "jp_type": "GUEST-OS-OPT", "emails": None},
          #{"jps": ACROPOLIS_JPS_MASTER["NO-PC-HA"], "payload": ACROPOLIS_PAYLOAD_NO_PC_HA_MAJOR_REL, "jp_type": "NO-PC-HA"},
          #{"jps": ACROPOLIS_JPS_MASTER["SCHEDULER-OPT"], "payload": ACROPOLIS_PAYLOAD_SCHEDULER_OPT_MAJOR_REL, "jp_type": "SCHEDULER-OPT", "emails": None},

          #NOT STABLE ##{"jps": ACROPOLIS_JPS_MASTER["SCHEDULER-UPGRADES-LCM"], "payload": ACROPOLIS_PAYLOAD_LCM_SCHEDULER_HYPERVISOR_ANY, "emails": None}

          {"jps": ACROPOLIS_JPS_NON_REG_HANDEDOVER["PC"], "payload": ACROPOLIS_PAYLOAD_PC_MAJOR_REL, "jp_type": "PC-OVA", "emails": None},
          {"jps": ACROPOLIS_JPS_NON_REG_HANDEDOVER["PC-OVA"], "payload": ACROPOLIS_PAYLOAD_PC_OVA_HYPERVISOR_ANY_MAJOR_REL,"jp_type": "PC-OVA", "emails": None},
          #{"jps": ACROPOLIS_JPS_NON_REG_HANDEDOVER["PC-SCALEOUT"], "payload": ACROPOLIS_PAYLOAD_PC_SCALEOUT_MAJOR_REL,"jp_type": "PC-SCALEOUT", "emails": None},

        ]


        if clone_from_flag == 'master':
            self.clone_from_jps.extend(self.clone_from_master_jps)
        if clone_from_flag == 'major':
            self.clone_from_jps.extend(self.clone_from_major_jps)

        self.job_profiles = [
            # NOT in USE ##{"jps": ACROPOLIS_JPS_MAJOR["SCHEDULER-UPGRADES-LCM"], "payload": ACROPOLIS_PAYLOAD_LCM_SCHEDULER_HYPERVISOR_ANY, "emails": None},

           #### Catalog ####
           {"jps": ACROPOLIS_JPS_MAJOR["PC-CATALOG"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_MAJOR_REL, "jp_type": "PC-CATALOG", "emails": CATALOG_EMAIL_LIST},
           {"jps": ACROPOLIS_JPS_MAJOR["PC-CATALOG-HYPERVISOR-ANY"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MAJOR_REL, "jp_type": "PC-CATALOG-HYPERVISOR-ANY", "emails": CATALOG_EMAIL_LIST},
           {"jps": ACROPOLIS_JPS_MAJOR["PE-CATALOG"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL, "jp_type": "PE-CATALOG", "emails": CATALOG_EMAIL_LIST},
           {"jps": ACROPOLIS_JPS_MAJOR["PC-CATALOG-ESX"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_ESX_MAJOR_REL, "jp_type": "PC-CATALOG-ESX", "emails": CATALOG_EMAIL_LIST},


            #### Acropolis ####
          #{"jps": ACROPOLIS_JPS_MAJOR["PC"], "payload": ACROPOLIS_PAYLOAD_PC_MAJOR_REL, "jp_type": "PC", "emails": None},
          #{"jps": ACROPOLIS_JPS_MAJOR["GUEST-OS-OTHERS"], "payload": ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_MAJOR_REL, "jp_type": "GUEST-OS-OTHERS", "emails": None},
          #{"jps": ACROPOLIS_JPS_MAJOR["NO-PC"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL, "jp_type": "NO-PC", "emails": None},
          #{"jps": ACROPOLIS_JPS_MAJOR["GPU"], "payload": ACROPOLIS_PAYLOAD_GPU_MAJOR_REL, "jp_type": "GPU", "emails": None},
          #{"jps": ACROPOLIS_JPS_MAJOR["VNUMA"], "payload": ACROPOLIS_PAYLOAD_VNUMA_MAJOR_REL, "jp_type": "VNUMA", "emails": None},


            #### Guest_OS ####
            #{"jps": ACROPOLIS_JPS_MAJOR["GUEST-OS-OPT"], "payload": ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MAJOR_REL, "jp_type": "GUEST-OS-OPT", "emails": None},

            #### Scheuler ####
            #{"jps": ACROPOLIS_JPS_MAJOR["SCHEDULER-OPT"], "payload": ACROPOLIS_PAYLOAD_SCHEDULER_OPT_MAJOR_REL, "jp_type": "SCHEDULER-OPT", "emails": None},
            #{"jps": ACROPOLIS_JPS_MAJOR["NO-PC-HA"], "payload": ACROPOLIS_PAYLOAD_NO_PC_HA_MAJOR_REL, "jp_type": "NO-PC-HA", "emails": None},

            #### OVA and Capabilities and Scaleout ####
           {"jps": ACROPOLIS_JPS_5_18["NON-REG-PC"], "payload": ACROPOLIS_PAYLOAD_PC_MAJOR_REL,  "jp_type": "PC-OVA", "emails": None},
           {"jps": ACROPOLIS_JPS_5_18["PC-OVA"], "payload": ACROPOLIS_PAYLOAD_PC_OVA_HYPERVISOR_ANY_MAJOR_REL, "jp_type": "PC-OVA", "emails": None},
           #{"jps": ACROPOLIS_JPS_5_18["PC-SCALEOUT"], "payload": ACROPOLIS_PAYLOAD_PC_SCALEOUT_MAJOR_REL, "jp_type": "PC-SCALEOUT", "emails": None},

        ]


class AcropolisMinor(QTMS):

    def __init__(self):
         QTMS.__init__(self)
         self.jita_operations = [
          # {"op": 'clone_job_profile', "fromBranch": 'master', "toBranch": '5.17.1'},
        #{"op": 'update_job_profile'},
        {"op": 'trigger_job_profile'}
         ]
         self.clone_from_jps = []
         self.clone_from_master_jps = []
         self.clone_from_major_jps = []
         self.clone_from_minor_jps = []

         clone_from_flag = "master"
         # clone_from_flag = "major"
         # clone_from_flag = "minor"

         self.clone_from_master_jps = [
              #{"jps": ACROPOLIS_JPS_MASTER["PC-CATALOG"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_MAJOR_REL, "jp_type": "PC-CATALOG", "emails": CATALOG_EMAIL_LIST},
              #{"jps": ACROPOLIS_JPS_MASTER["PC-CATALOG-HYPERVISOR-ANY"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MAJOR_REL, "jp_type": "PC-CATALOG-HYPERVISOR-ANY", "emails": CATALOG_EMAIL_LIST},
              #{ "jps": ACROPOLIS_JPS_MASTER["PC-CATALOG-ESX"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_ESX_MASTER, "jp_type": "PC-CATALOG-ESX", "emails": CATALOG_EMAIL_LIST},
              #{"jps": ACROPOLIS_JPS_MASTER["PE-CATALOG"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL, "jp_type": "PE-CATALOG", "emails": CATALOG_EMAIL_LIST},

              {"jps": ACROPOLIS_JPS_MASTER["PC"], "payload": ACROPOLIS_PAYLOAD_PC_MAJOR_REL, "jp_type": "PC", "emails": None},
              {"jps": ACROPOLIS_JPS_MASTER["GUEST-OS-OTHERS"], "payload": ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_MAJOR_REL, "jp_type": "GUEST-OS-OTHERS", "emails": None},
              {"jps": ACROPOLIS_JPS_MASTER["NO-PC"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MAJOR_REL, "jp_type": "NO-PC", "emails": None},
              {"jps": ACROPOLIS_JPS_MASTER["GPU"], "payload": ACROPOLIS_PAYLOAD_GPU_MAJOR_REL, "jp_type": "GPU", "emails": None},
              {"jps": ACROPOLIS_JPS_MASTER["VNUMA"], "payload": ACROPOLIS_PAYLOAD_VNUMA_MAJOR_REL, "jp_type": "VNUMA", "emails": None},
#              {"jps": ACROPOLIS_JPS_MASTER["Xi-MGMT"], "payload": ACROPOLIS_PAYLOAD_PC_MAJOR_REL, "jp_type": "Xi-MGMT", "emails": None},

              {"jps": ACROPOLIS_JPS_MASTER["GUEST-OS-OPT"], "payload": ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MAJOR_REL, "jp_type": "GUEST-OS-OPT", "emails": None},
              {"jps": ACROPOLIS_JPS_MASTER["NO-PC-HA"], "payload": ACROPOLIS_PAYLOAD_NO_PC_HA_MAJOR_REL, "jp_type": "NO-PC-HA"},
              {"jps": ACROPOLIS_JPS_MASTER["SCHEDULER-OPT"], "payload": ACROPOLIS_PAYLOAD_SCHEDULER_OPT_MAJOR_REL, "jp_type": "SCHEDULER-OPT", "emails": None},

         ]

         self.clone_from_major_jps = [
             # {"jps": ACROPOLIS_JPS_MAJOR["NO-PC"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL, "jp_type": "NO-PC"},
             # {"jps": ACROPOLIS_JPS_MAJOR["NO-PC-HA"], "payload": ACROPOLIS_PAYLOAD_NO_PC_HA_MINOR_REL, "jp_type": "NO-PC-HA"},
             # {"jps": ACROPOLIS_JPS_MAJOR["PC"], "payload": ACROPOLIS_PAYLOAD_PC_MINOR_REL, "jp_type": "PC"},
             # {"jps": ACROPOLIS_JPS_MAJOR["GPU"], "payload": ACROPOLIS_PAYLOAD_GPU_MINOR_REL, "jp_type": "GPU"},
             # {"jps": ACROPOLIS_JPS_MAJOR["VNUMA"], "payload": ACROPOLIS_PAYLOAD_VNUMA_MINOR_REL, "jp_type": "VNUMA"},
             # {"jps": ACROPOLIS_JPS_MAJOR["GUEST-OS"], "payload": ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_MINOR_REL, "jp_type": "GUEST-OS"}
            ]

         self.clone_from_minor_jps = [
             # {"jps": ACROPOLIS_JPS_MINOR["NO-PC"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL, "jp_type": "NO-PC"},
             # {"jps": ACROPOLIS_JPS_MINOR["NO-PC-HA"], "payload": ACROPOLIS_PAYLOAD_NO_PC_HA_MINOR_REL,  "jp_type": "NO-PC-HA"},
             # {"jps": ACROPOLIS_JPS_MINOR["PC"], "payload": ACROPOLIS_PAYLOAD_PC_MINOR_REL,  "jp_type": "PC"},
             # {"jps": ACROPOLIS_JPS_MINOR["GPU"], "payload": ACROPOLIS_PAYLOAD_GPU_MINOR_REL,  "jp_type": "GPU"},
             # {"jps": ACROPOLIS_JPS_MINOR["VNUMA"], "payload": ACROPOLIS_PAYLOAD_VNUMA_MINOR_REL,  "jp_type": "VNUMA"},
             # {"jps": ACROPOLIS_JPS_MINOR["GUEST-OS"], "payload": ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_MINOR_REL,  "jp_type": "GUEST-OS"}
            ]

         if clone_from_flag == 'master':
             self.clone_from_jps.extend(self.clone_from_master_jps)
         if clone_from_flag == 'major':
             self.clone_from_jps.extend(self.clone_from_major_jps)
         if clone_from_flag == 'minor':
             self.clone_from_jps.extend(self.clone_from_minor_jps)

         self.job_profiles = [

             #### Catalog #####
            #{"jps": ACROPOLIS_JPS_MINOR["PC-CATALOG"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_MINOR, "jp_type": "PC-CATALOG", "emails": CATALOG_EMAIL_LIST},
            #{"jps": ACROPOLIS_JPS_MINOR["PC-CATALOG-HYPERVISOR-ANY"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MINOR, "jp_type": "PC-CATALOG-HYPERVISOR-ANY", "emails": CATALOG_EMAIL_LIST},
            #{"jps": ACROPOLIS_JPS_MINOR["PE-CATALOG"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL, "jp_type": "PE-CATALOG", "emails": CATALOG_EMAIL_LIST},
            #{"jps": ACROPOLIS_JPS_MINOR["PC-CATALOG-ESX"], "payload": ACROPOLIS_PAYLOAD_PC_CATALOG_ESX_MINOR, "jp_type": "PC-CATALOG-ESX", "emails": CATALOG_EMAIL_LIST},

            #### Acropolis ####
            #{"jps": ACROPOLIS_JPS_MINOR["PC"], "payload": ACROPOLIS_PAYLOAD_PC_MINOR_REL, "jp_type": "PC", "emails": None},
            #{"jps": ACROPOLIS_JPS_MINOR["GUEST-OS-OTHERS"], "payload": ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_MINOR_REL, "jp_type": "GUEST-OS-OTHERS", "emails": None},
            #{"jps": ACROPOLIS_JPS_MINOR["NO-PC"], "payload": ACROPOLIS_PAYLOAD_NO_PC_MINOR_REL, "jp_type": "NO-PC", "emails": None},
            #{"jps": ACROPOLIS_JPS_MINOR["GPU"], "payload": ACROPOLIS_PAYLOAD_GPU_MINOR_REL, "jp_type": "GPU", "emails": None},
            #{"jps": ACROPOLIS_JPS_MINOR["VNUMA"], "payload": ACROPOLIS_PAYLOAD_VNUMA_MINOR_REL, "jp_type": "VNUMA", "emails": None},

            ### Xi-Mgmt ###
            #{"jps": ACROPOLIS_JPS_MINOR["Xi-MGMT"], "payload": ACROPOLIS_PAYLOAD_PC_MINOR_REL, "jp_type": "Xi-MGMT", "emails": None},

            #### Guest_Os ####
           # {"jps": ACROPOLIS_JPS_MINOR["GUEST-OS-OPT"], "payload": ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MINOR_REL, "jp_type": "GUEST-OS-OPT", "emails": None},

            #### Scheduler ####
            {"jps": ACROPOLIS_JPS_MINOR["NO-PC-HA"], "payload": ACROPOLIS_PAYLOAD_NO_PC_HA_MINOR_REL, "jp_type": "NO-PC-HA"},
            {"jps": ACROPOLIS_JPS_MINOR["SCHEDULER-OPT"], "payload": ACROPOLIS_PAYLOAD_SCHEDULER_OPT_MINOR_REL, "jp_type": "SCHEDULER-OPT", "emails": None},
         ]


class UhuraMaster(QTMS):

    def __init__(self):
        QTMS.__init__(self)
        self.jita_operations = [
       #{"op": 'update_job_profile'},
       {"op": 'trigger_job_profile'}
        ]
        self.job_profiles = [
            {"jps": UHURA_JPS_MASTER["NO-PC-WITH-VC"], "payload": UHURA_PAYLOAD_NO_PC_WITH_VC_MASTER, "emails": None},
            #{"jps": UHURA_JPS_MASTER["NO-PC-NO-VC"], "payload": UHURA_PAYLOAD_NO_PC_NO_VC_MASTER, "emails": None},
           # {"jps": UHURA_JPS_MASTER["PC"], "payload": UHURA_PAYLOAD_PC_MASTER, "emails": None},
            {"jps": UHURA_JPS_MASTER["NS-WITH-VC"], "payload": UHURA_PAYLOAD_NS_WITH_VC_MASTER, "emails": None},
            #{"jps": UHURA_JPS_MASTER["NS-NO-VC"], "payload": UHURA_PAYLOAD_NS_NO_VC_MASTER, "emails": None}
        ]


class UhuraMajor(QTMS):

    def __init__(self):
        QTMS.__init__(self)
        self.jita_operations = [
            #{"op": 'clone_job_profile', "fromBranch": 'master', "toBranch": '5.18'},
            {"op": 'update_job_profile'},
            #{"op": 'trigger_job_profile'}
        ]
        self.clone_from_jps = [
            {"jps": UHURA_JPS_MASTER["NO-PC-WITH-VC"], "payload": UHURA_PAYLOAD_NO_PC_WITH_VC_MAJOR_REL, 'jp_type': "NO-PC-WITH-VC"},
            {"jps": UHURA_JPS_MASTER["NO-PC-NO-VC"], "payload": UHURA_PAYLOAD_NO_PC_NO_VC_MAJOR_REL, 'jp_type': "NO-PC-NO-VC"},
            {"jps": UHURA_JPS_MASTER["PC"], "payload": UHURA_PAYLOAD_PC_MAJOR_REL, 'jp_type': "PC"},
            {"jps": UHURA_JPS_MASTER["NS-WITH-VC"],  "payload": UHURA_PAYLOAD_NS_WITH_VC_MAJOR_REL, 'jp_type': "NS-WITH-VC"},
            {"jps": UHURA_JPS_MASTER["NS-NO-VC"], "payload": UHURA_PAYLOAD_NS_NO_VC_MAJOR_REL, 'jp_type': "NS-NO-VC"}
        ]

        # self.clone_from_jps = [
        #     {"jps": UHURA_JPS_MINOR["NO-PC-WITH-VC"], "payload": UHURA_PAYLOAD_NO_PC_WITH_VC_MAJOR_REL, 'jp_type': "NO-PC-WITH-VC"},
        #     {"jps": UHURA_JPS_MINOR["NO-PC-NO-VC"], "payload": UHURA_PAYLOAD_NO_PC_NO_VC_MAJOR_REL, 'jp_type': "NO-PC-NO-VC"},
        #     {"jps": UHURA_JPS_MINOR["PC"], "payload": UHURA_PAYLOAD_PC_MAJOR_REL, 'jp_type': "PC"},
        #     {"jps": UHURA_JPS_MINOR["NS-WITH-VC"],  "payload": UHURA_PAYLOAD_NS_WITH_VC_MAJOR_REL, 'jp_type': "NS-WITH-VC"},
        #     {"jps": UHURA_JPS_MINOR["NS-NO-VC"], "payload": UHURA_PAYLOAD_NS_NO_VC_MAJOR_REL, 'jp_type': "NS-NO-VC"}
        # ]

        self.job_profiles = [
            {"jps": UHURA_JPS_MAJOR["NO-PC-WITH-VC"], "payload": UHURA_PAYLOAD_NO_PC_WITH_VC_MAJOR_REL, "emails": None},
            {"jps": UHURA_JPS_MAJOR["NO-PC-NO-VC"], "payload": UHURA_PAYLOAD_NO_PC_NO_VC_MAJOR_REL, "emails": None},
           {"jps": UHURA_JPS_MAJOR["PC"], "payload": UHURA_PAYLOAD_PC_MAJOR_REL, "emails": None},
            {"jps": UHURA_JPS_MAJOR["NS-WITH-VC"], "payload": UHURA_PAYLOAD_NS_WITH_VC_MAJOR_REL, "emails": None},
            {"jps": UHURA_JPS_MAJOR["NS-NO-VC"], "payload": UHURA_PAYLOAD_NS_NO_VC_MAJOR_REL, "emails": None}
        ]


class UhuraMinor(QTMS):

    def __init__(self):
        QTMS.__init__(self)
        self.jita_operations = [
          #{"op": 'clone_job_profile', "fromBranch": 'master', "toBranch": '5.17.1'},
        #{"op": 'update_job_profile'},
         {"op": 'trigger_job_profile'}
        ]

        # self.clone_from_jps = [
        #     {"jps": UHURA_JPS_MINOR["NO-PC-WITH-VC"], "payload": UHURA_PAYLOAD_NO_PC_WITH_VC_MAJOR_REL, 'jp_type': "NO-PC-WITH-VC"},
        #     {"jps": UHURA_JPS_MINOR["NO-PC-NO-VC"], "payload": UHURA_PAYLOAD_NO_PC_NO_VC_MAJOR_REL, 'jp_type': "NO-PC-NO-VC"},
        #     {"jps": UHURA_JPS_MINOR["PC"], "payload": UHURA_PAYLOAD_PC_MAJOR_REL, 'jp_type': "PC"},
        #     {"jps": UHURA_JPS_MINOR["NS-WITH-VC"],  "payload": UHURA_PAYLOAD_NS_WITH_VC_MAJOR_REL, 'jp_type': "NS-WITH-VC"},
        #     {"jps": UHURA_JPS_MINOR["NS-NO-VC"], "payload": UHURA_PAYLOAD_NS_NO_VC_MAJOR_REL, 'jp_type': "NS-NO-VC"}
        # ]

        self.clone_from_jps = [
            #{"jps": UHURA_JPS_MASTER["NO-PC-WITH-VC"], "payload": UHURA_PAYLOAD_NO_PC_WITH_VC_MASTER, 'jp_type': "NO-PC-WITH-VC"},
            #{"jps": UHURA_JPS_MASTER["NO-PC-NO-VC"], "payload": UHURA_PAYLOAD_NO_PC_NO_VC_MASTER, 'jp_type': "NO-PC-NO-VC"},
            {"jps": UHURA_JPS_MASTER["PC"], "payload": UHURA_PAYLOAD_PC_MASTER, 'jp_type': "PC"},
            #{"jps": UHURA_JPS_MASTER["NS-WITH-VC"],  "payload": UHURA_PAYLOAD_NS_WITH_VC_MASTER, 'jp_type': "NS-WITH-VC"},
            #{"jps": UHURA_JPS_MASTER["NS-NO-VC"], "payload": UHURA_PAYLOAD_NS_NO_VC_MASTER, 'jp_type': "NS-NO-VC"}
        ]

        self.job_profiles = [
            {"jps": UHURA_JPS_MINOR["NO-PC-WITH-VC"], "payload": UHURA_PAYLOAD_NO_PC_WITH_VC_MINOR_REL},
            {"jps": UHURA_JPS_MINOR["NO-PC-NO-VC"], "payload": UHURA_PAYLOAD_NO_PC_NO_VC_MINOR_REL},
            {"jps": UHURA_JPS_MINOR["PC"], "payload": UHURA_PAYLOAD_PC_MINOR_REL},
            {"jps": UHURA_JPS_MINOR["NS-WITH-VC"], "payload": UHURA_PAYLOAD_NS_WITH_VC_MINOR_REL},
            {"jps": UHURA_JPS_MINOR["NS-NO-VC"], "payload": UHURA_PAYLOAD_NS_NO_VC_MINOR_REL}
        ]


class AcropolisMR(QTMS):

    def __init__(self):
        QTMS.__init__(self)
        self.jita_operations = [
#            {"op": 'clone_job_profile', "fromBranch": '', "toBranch": ''},
#            {"op": 'update_job_profile'},
            {"op": 'trigger_job_profile'}
        ]
        self.job_profiles = [
            {"jps": ACROPOLIS_JPS_LTS["GUEST-OS"], "payload": ACROPOLIS_PAYLOAD_NO_PC_GUEST_OS_LTS},
            {"jps": ACROPOLIS_JPS_LTS["NO-PC"], "payload": ACROPOLIS_PAYLOAD_NO_PC_LTS},
            {"jps": ACROPOLIS_JPS_LTS["GPU"], "payload": ACROPOLIS_PAYLOAD_GPU_LTS},
#            {"jps": ACROPOLIS_JPS_LTS["VNUMA"], "payload": ACROPOLIS_PAYLOAD_VNUMA_LTS},
            {"jps": ACROPOLIS_JPS_LTS["NO-PC-HA"], "payload": ACROPOLIS_PAYLOAD_NO_PC_HA_LTS}
        ]


class UhuraMR(QTMS):

    def __init__(self):
        QTMS.__init__(self)
        self.jita_operations = [
#            {"op": 'clone_job_profile', "fromBranch": '', "toBranch": ''},
#            {"op": 'update_job_profile'},
            {"op": 'trigger_job_profile'}
        ]
        self.job_profiles = [
            {"jps": UHURA_JPS_LTS["NO-PC-WITH-VC"], "payload": UHURA_PAYLOAD_NO_PC_WITH_VC_LTS},
            {"jps": UHURA_JPS_LTS["NO-PC-NO-VC"], "payload": UHURA_PAYLOAD_NO_PC_NO_VC_LTS},
            {"jps": UHURA_JPS_LTS["NS-NO-VC"], "payload": UHURA_PAYLOAD_NS_NO_VC_LTS},
            {"jps": UHURA_JPS_LTS["NS-WITH-VC"], "payload": UHURA_PAYLOAD_NS_WITH_VC_LTS}
        ]


class AHVGoldSuitePatch(QTMS):

    def __init__(self):
        QTMS.__init__(self)
        self.jita_operations = [
          {"op": 'update_job_profile'},
         # {"op": 'trigger_job_profile'}
        ]
        self.job_profiles = [
            {"jps": GOLD_SUITE_JPS["PC"], "payload": GOLD_SUITE_PAYLOAD_PC, "emails": CATALOG_EMAIL_LIST},
            {"jps": GOLD_SUITE_JPS["NO-PC"], "payload": GOLD_SUITE_PAYLOAD_NO_PC, "emails": None},
           {"jps": GOLD_SUITE_JPS["GPU"], "payload": GOLD_SUITE_PAYLOAD_GPU, "emails": None},
           {"jps": GOLD_SUITE_JPS["UHURA"], "payload": GOLD_SUITE_PAYLOAD_UHURA, "emails": None}
        ]


class AHVCompatibilityTest(QTMS):

    def __init__(self):
        QTMS.__init__(self)
        self.component = "Metropolis"
        self.compatibility_matrix = [
#            {"pe": "5.5.9", "pc": "5.10.2"},
#            {"pe": "5.5.9", "pc": "5.9.2"}
#             {"pe": "5.8.2", "pc": "5.10.2"},
#             {"pe": "5.9.2", "pc": "5.10.2"},
#             {"pe": "5.8.2", "pc": "5.10.3"},
#             {"pe": "5.9.2", "pc": "5.10.3"},
#             {"pe": "5.5.9", "pc": "5.10.3"},
#              {"pe": "5.5.9", "pc": "5.11"},
#              {"pe": "5.9.2", "pc": "5.11"},
#              {"pe": "5.10.2", "pc": "5.11"},
            #{"pe": "5.10.4", "pc": "5.11"}
            {"pe": "5.5.9", "pc": "5.10.5"},
            {"pe": "5.8.2", "pc": "5.10.5"},
            {"pe": "5.9.2", "pc": "5.10.5"},
            #{"pe": "5.10.5", "pc": "5.11"}

        ]
        self.jita_operations = [
            {"op": 'create_compatibility_jps'}
        ]



if __name__ == '__main__':
    qtms_operations = [
        'kill_jita_tasks',
        'get_node_pool_utilization',
        'rel_sp_operations'
    ]

    rel_class = [
    #'AcropolisMaster',
 #   'AcropolisMasterNonRegHandedover',
  #'AcropolisMajor',
   'AcropolisMinor',
    #'UhuraMaster',
    #'UhuraMajor',
   # 'UhuraMinor',
#        'AcropolisMR',
#        'UhuraMR',
        #'AHVGoldSuitePatch',
#        'AHVCompatibilityTest'
        ]

    qtms_runner = QTMSRunner(rel_class, qtms_operations)
    qtms_runner.qtms_run()
