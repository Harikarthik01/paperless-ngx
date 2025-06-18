from documents.tests.utils import DirectoriesMixin
from documents.tests.utils import TestMigrations


class TestMigrateScheduledWorkflowTrigger(DirectoriesMixin, TestMigrations):
    migrate_from = "1065_workflowaction_assign_custom_fields_values"
    migrate_to = "1066_alter_workflowtrigger_schedule_offset_days"

    def setUpBeforeMigration(self, apps):
        WorkflowTrigger = apps.get_model("documents", "WorkflowTrigger")
        WorkflowTrigger.objects.create(
            type=4,
            schedule_offset_days=5,
        )

    def testTriggerMigrated(self):
        WorkflowTrigger = self.apps.get_model("documents", "WorkflowTrigger")
        trigger = WorkflowTrigger.objects.get(id=1)
        self.assertEqual(trigger.schedule_offset_days, -5)
