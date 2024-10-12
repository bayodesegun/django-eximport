from django.core.management.base import BaseCommand
from pilotlog.models import PilotLog
from pilotlog.utils import JSONImporter


class Command(BaseCommand):
    help = "Import data from JSON file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file-path",
            type=str,
            required=True,
            help="Path to JSON file"
        )

    def handle(self, *args, **options):
        if not options["file_path"]:
            raise ValueError("File path is required")

        for field in PilotLog._meta.fields:
            db_column = field.get_attname_column()[1]
            print(f"{db_column}: {field.verbose_name}")

        JSONImporter(options["file_path"]).import_data()
