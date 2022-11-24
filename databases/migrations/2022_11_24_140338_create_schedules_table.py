"""CreateSchedulesTable Migration."""

from masoniteorm.migrations import Migration


class CreateSchedulesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("schedules") as table:
            table.increments("id")
            table.datetime("start_time")

            table.integer("event_id").unsigned()
            table.foreign("event_id").references("id").on("events").on_delete('cascade')

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("schedules")
