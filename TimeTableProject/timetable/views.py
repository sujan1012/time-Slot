from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField
from .models import TimeSlot


def timetable_view(request):

    timetable_records = TimeSlot.objects.all().annotate(
        day_order=Case(
            When(day='Monday', then=Value(1)),
            When(day='Tuesday', then=Value(2)),
            When(day='Wednesday', then=Value(3)),
            When(day='Thursday', then=Value(4)),
            When(day='Friday', then=Value(5)),
            When(day='Saturday', then=Value(6)),
            output_field=IntegerField()
        )
    ).order_by('day_order', 'start_time')

    context = {
        'timetable': timetable_records
    }

    return render(request, 'timetable/timetable.html', context)

# Create your views here.
