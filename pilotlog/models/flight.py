from django.db import models
from .bases import RecordTracking


class Flight(RecordTracking):
    flight_code = models.CharField(
        max_length=36,
        primary_key=True,
        verbose_name="FlightCode",
        help_text="Unique identifier for this flight"
    )
    aircraft = models.ForeignKey(
        "Aircraft", on_delete=models.PROTECT,
        verbose_name="Aircraft",
        db_column="aircraft_code",
        help_text="Unique identifier for the aircraft used in this flight"
    )
    arr_code = models.CharField(
        max_length=36,
        verbose_name="ArrCode",
        help_text="Code for the arrival airport"
    )
    arr_offset = models.IntegerField(
        verbose_name="ArrOffset",
        help_text="Time offset for the arrival location"
    )
    arr_rwy = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="ArrRwy",
        help_text="Arrival runway designation"
    )
    arr_time_sched = models.IntegerField(
        verbose_name="ArrTimeSCHED",
        help_text="Scheduled arrival time"
    )
    arr_time_utc = models.IntegerField(
        verbose_name="ArrTimeUTC",
        help_text="Actual arrival time in UTC"
    )
    base_offset = models.IntegerField(
        verbose_name="BaseOffset",
        help_text="Time offset for the base location"
    )
    crew_list = models.TextField(
        blank=True,
        verbose_name="CrewList",
        help_text="List of crew members on the flight"
    )
    date_base = models.DateField(
        verbose_name="DateBASE",
        help_text="Date of the flight in the base time zone"
    )
    date_local = models.DateField(
        verbose_name="DateLOCAL",
        help_text="Date of the flight in the local time zone"
    )
    date_utc = models.DateField(
        verbose_name="DateUTC",
        help_text="Date of the flight in UTC"
    )
    de_ice = models.BooleanField(
        verbose_name="DeIce",
        help_text="Indicates if de-icing was performed"
    )
    dep_code = models.CharField(
        max_length=36,
        verbose_name="DepCode",
        help_text="Code for the departure airport"
    )
    dep_offset = models.IntegerField(
        verbose_name="DepOffset",
        help_text="Time offset for the departure location"
    )
    dep_rwy = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="DepRwy",
        help_text="Departure runway designation"
    )
    dep_time_sched = models.IntegerField(
        verbose_name="DepTimeSCHED",
        help_text="Scheduled departure time"
    )
    dep_time_utc = models.IntegerField(
        verbose_name="DepTimeUTC",
        help_text="Actual departure time in UTC"
    )
    flight_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="FlightNumber",
        help_text="Flight number or designation"
    )
    flight_search = models.CharField(
        max_length=255,
        verbose_name="FlightSearch",
        help_text="Search key for the flight"
    )
    fuel = models.FloatField(
        verbose_name="Fuel",
        help_text="Amount of fuel on board"
    )
    fuel_planned = models.FloatField(
        verbose_name="FuelPlanned",
        help_text="Planned amount of fuel for the flight"
    )
    fuel_used = models.FloatField(
        verbose_name="FuelUsed",
        help_text="Amount of fuel used during the flight"
    )
    hobbs_in = models.FloatField(
        verbose_name="HobbsIn",
        help_text="Hobbs meter reading at the end of the flight"
    )
    hobbs_out = models.FloatField(
        verbose_name="HobbsOut",
        help_text="Hobbs meter reading at the start of the flight"
    )
    holding = models.IntegerField(
        verbose_name="Holding",
        help_text="Time spent in holding patterns"
    )
    ldg_day = models.IntegerField(
        verbose_name="LdgDay",
        help_text="Number of day landings"
    )
    ldg_night = models.IntegerField(
        verbose_name="LdgNight",
        help_text="Number of night landings"
    )
    ldg_time_utc = models.IntegerField(
        verbose_name="LdgTimeUTC",
        help_text="Landing time in UTC"
    )
    lift_sw = models.IntegerField(
        verbose_name="LiftSW",
        help_text="Lift switch status"
    )
    next_page = models.BooleanField(
        verbose_name="NextPage",
        help_text="Indicates if there is a next page in the log"
    )
    next_summary = models.BooleanField(
        verbose_name="NextSummary",
        help_text="Indicates if there is a next summary"
    )
    p1_code = models.CharField(
        max_length=36,
        verbose_name="P1Code",
        help_text="Code for the first pilot"
    )
    p2_code = models.CharField(
        max_length=36,
        verbose_name="P2Code",
        help_text="Code for the second pilot"
    )
    p3_code = models.CharField(
        max_length=36,
        verbose_name="P3Code",
        help_text="Code for the third pilot"
    )
    p4_code = models.CharField(
        max_length=36,
        verbose_name="P4Code",
        help_text="Code for the fourth pilot"
    )
    pf = models.BooleanField(
        verbose_name="PF",
        help_text="Indicates if the pilot was Pilot Flying"
    )
    pairing = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Pairing",
        help_text="Flight pairing information"
    )
    pax = models.IntegerField(
        verbose_name="Pax",
        help_text="Number of passengers on board"
    )
    remarks = models.TextField(
        verbose_name="Remarks",
        help_text="Additional remarks about the flight"
    )
    report = models.TextField(
        blank=True,
        verbose_name="Report",
        help_text="Flight report details"
    )
    route = models.TextField(
        blank=True,
        verbose_name="Route",
        help_text="Flight route information"
    )
    sign_box = models.IntegerField(
        verbose_name="SignBox",
        help_text="Signature box status"
    )
    tag_approach = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="TagApproach",
        help_text="Approach tag for the flight"
    )
    tag_delay = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="TagDelay",
        help_text="Delay tag for the flight"
    )
    tag_launch = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="TagLaunch",
        help_text="Launch tag for the flight"
    )
    tag_lesson = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="TagLesson",
        help_text="Lesson tag for the flight"
    )
    tag_ops = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="TagOps",
        help_text="Operations tag for the flight"
    )
    to_day = models.IntegerField(
        verbose_name="ToDay",
        help_text="Number of day takeoffs"
    )
    to_edit = models.BooleanField(
        verbose_name="ToEdit",
        help_text="Indicates if the entry is editable"
    )
    to_night = models.IntegerField(
        verbose_name="ToNight",
        help_text="Number of night takeoffs"
    )
    to_time_utc = models.IntegerField(
        verbose_name="ToTimeUTC",
        help_text="Takeoff time in UTC"
    )
    training = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Training",
        help_text="Training information for the flight"
    )
    user_bool = models.BooleanField(
        verbose_name="UserBool",
        help_text="User-defined boolean field"
    )
    user_num = models.IntegerField(
        verbose_name="UserNum",
        help_text="User-defined numeric field"
    )
    user_text = models.TextField(
        blank=True,
        verbose_name="UserText",
        help_text="User-defined text field"
    )
    min_air = models.IntegerField(
        verbose_name="minAIR",
        help_text="Minimum air time in minutes"
    )
    min_cop = models.IntegerField(
        verbose_name="minCOP",
        help_text="Minimum co-pilot time in minutes"
    )
    min_dual = models.IntegerField(
        verbose_name="minDUAL",
        help_text="Minimum dual instruction time in minutes"
    )
    min_exam = models.IntegerField(
        verbose_name="minEXAM",
        help_text="Minimum examination time in minutes"
    )
    min_ifr = models.IntegerField(
        verbose_name="minIFR",
        help_text="Minimum IFR time in minutes"
    )
    min_imt = models.IntegerField(
        verbose_name="minIMT",
        help_text="Minimum instrument time in minutes"
    )
    min_instr = models.IntegerField(
        verbose_name="minINSTR",
        help_text="Minimum instruction time in minutes"
    )
    min_night = models.IntegerField(
        verbose_name="minNIGHT",
        help_text="Minimum night time in minutes"
    )
    min_pic = models.IntegerField(
        verbose_name="minPIC",
        help_text="Minimum Pilot-in-Command time in minutes"
    )
    min_picus = models.IntegerField(
        verbose_name="minPICUS",
        help_text="Minimum Pilot-in-Command Under Supervision time in minutes"
    )
    min_rel = models.IntegerField(
        verbose_name="minREL",
        help_text="Minimum relief pilot time in minutes"
    )
    min_sfr = models.IntegerField(
        verbose_name="minSFR",
        help_text="Minimum Special Flight Rules time in minutes"
    )
    min_total = models.IntegerField(
        verbose_name="minTOTAL",
        help_text="Total flight time in minutes"
    )
    min_u1 = models.IntegerField(
        verbose_name="minU1",
        help_text="User-defined time 1 in minutes"
    )
    min_u2 = models.IntegerField(
        verbose_name="minU2",
        help_text="User-defined time 2 in minutes"
    )
    min_u3 = models.IntegerField(
        verbose_name="minU3",
        help_text="User-defined time 3 in minutes"
    )
    min_u4 = models.IntegerField(
        verbose_name="minU4",
        help_text="User-defined time 4 in minutes"
    )
    min_xc = models.IntegerField(
        verbose_name="minXC",
        help_text="Minimum cross-country time in minutes"
    )

    def __str__(self):
        return f"Flight {self.flight_code}"

    class Meta:
        verbose_name = "Flight"
        verbose_name_plural = "Flights"
