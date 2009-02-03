from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = "Import open-bookings users and profiles as django users and groups."
    
    def handle_noargs(self, **options):
        print "Not Yet Implemented."