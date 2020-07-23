# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airport(models.Model):
    a_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    altitude = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    dgm = models.OneToOneField('Dgm', models.DO_NOTHING, blank=True, null=True)
    longitude = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.CharField(max_length=10, blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airport'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField()
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.OneToOneField('Supervisor', models.DO_NOTHING, db_column='username', primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Cdvordaily(models.Model):
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    azimuth_angle = models.IntegerField(db_column='Azimuth_angle', blank=True, null=True)  # Field name made lowercase.
    number_30hz_modulation = models.IntegerField(db_column='30Hz_modulation', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_9960hz_modulation = models.IntegerField(db_column='9960Hz_modulation', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_9960hz_deviation = models.IntegerField(db_column='9960Hz_deviation', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    field_intensity = models.IntegerField(blank=True, null=True)
    ident_modulation = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    f_id = models.CharField(max_length=10)
    p_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=30)
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cdvordaily'

class Cdvordlogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING)
    p = models.ForeignKey('Cdvordaily', models.DO_NOTHING)
    value = models.CharField(max_length=30)
    remarks = models.CharField(db_column='Remarks', max_length=100)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'cdvordlogs'



class Cdvormonthly(models.Model):
    p_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    f_id = models.CharField(max_length=10)
    status = models.CharField(max_length=30)
    measured_bearing_1 = models.FloatField(blank=True, null=True)
    bearing_deviation_1 = models.FloatField(blank=True, null=True)
    measured_bearing_2 = models.FloatField(blank=True, null=True)
    bearing_deviation_2 = models.FloatField(blank=True, null=True)
    measured_bearing_3 = models.FloatField(blank=True, null=True)
    bearing_deviation_3 = models.FloatField(blank=True, null=True)
    measured_bearing_4 = models.FloatField(blank=True, null=True)
    bearing_deviation_4 = models.FloatField(blank=True, null=True)
    measured_bearing_5 = models.FloatField(blank=True, null=True)
    bearing_deviation_5 = models.FloatField(blank=True, null=True)
    error_spread = models.FloatField(blank=True, null=True)
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cdvormonthly'

class Cdvormlogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING)
    p = models.ForeignKey('Cdvormonthly', models.DO_NOTHING)
    value = models.CharField(max_length=30)
    remarks = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'cdvormlogs'        


class Cdvorweekly(models.Model):
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    f_id = models.CharField(max_length=10)
    p_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=30)
    ps_5v = models.FloatField(db_column='PS_5V', blank=True, null=True)  # Field name made lowercase.
    ps_12v = models.FloatField(db_column='PS_12V', blank=True, null=True)  # Field name made lowercase.
    ps_negative_12v = models.IntegerField(db_column='PS_negative_12V', blank=True, null=True)  # Field name made lowercase.
    ps_28v = models.IntegerField(db_column='PS_28V', blank=True, null=True)  # Field name made lowercase.
    ps_48v = models.IntegerField(db_column='PS_48V', blank=True, null=True)  # Field name made lowercase.
    outside_temp = models.IntegerField(blank=True, null=True)
    tx1_temp = models.IntegerField(db_column='TX1_temp', blank=True, null=True)  # Field name made lowercase.
    tx2_temp = models.IntegerField(db_column='TX2_temp', blank=True, null=True)  # Field name made lowercase.
    out_temp_enabled = models.CharField(db_column='Out_temp_enabled', max_length=10, blank=True, null=True)  # Field name made lowercase.
    am = models.IntegerField(db_column='AM', blank=True, null=True)  # Field name made lowercase.
    fm = models.IntegerField(db_column='FM', blank=True, null=True)  # Field name made lowercase.
    sideband_frequency = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cdvorweekly'
    
class Cdvorwlogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING)
    p = models.ForeignKey('Cdvorweekly', models.DO_NOTHING)
    value = models.CharField(max_length=30)
    remarks = models.CharField(db_column='Remarks', max_length=100)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'cdvorwlogs'

class Communication(models.Model):
    f_id = models.IntegerField(primary_key=True)
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    facility = models.CharField(max_length=20, blank=True, null=True)
    make = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    doi = models.DateField(db_column='DOI', blank=True, null=True)  # Field name made lowercase.
    doc = models.DateField(db_column='DOC', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=20, blank=True, null=True)
    supervisor = models.ForeignKey('Supervisor', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication'
        unique_together = (('f_id', 'a'), ('f_id', 'a'),)


class Datisdaily(models.Model):
    p_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    a = models.ForeignKey(Airport, models.DO_NOTHING, blank=True, null=True)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=40)  # Field name made lowercase.
    f = models.ForeignKey(Communication, models.DO_NOTHING, blank=True, null=True)
    room_temp = models.IntegerField(blank=True, null=True)
    status_of_ac = models.CharField(db_column='status_of_AC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status_of_ups = models.CharField(db_column='status_of_UPS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status_of_servera = models.CharField(db_column='status_of_serverA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status_of_serverb = models.CharField(db_column='status_of_serverB', max_length=10, blank=True, null=True)  # Field name made lowercase.
    datetime_of_servers_wrt_gps_clk = models.CharField(db_column='datetime_of_servers_wrt_GPS_CLK', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status_of_disk_array = models.CharField(db_column='status_of_Disk_array', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vhftx_atis_status = models.CharField(db_column='VHFTX_ATIS_status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vhfrx_atis_status = models.CharField(db_column='VHFRX_ATIS_status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    datis_update = models.CharField(db_column='DATIS_update', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audio_quality = models.CharField(db_column='Audio_quality', max_length=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datisdaily'
        unique_together = (('date', 'a'),)


class Datisdlogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING)
    p = models.ForeignKey(Datisdaily, models.DO_NOTHING)
    value = models.CharField(max_length=30)
    remarks = models.CharField(db_column='Remarks', max_length=100)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'datisdlogs'


class Datisweekly(models.Model):
    p_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    a = models.ForeignKey(Airport, models.DO_NOTHING, blank=True, null=True)
    f = models.ForeignKey(Communication, models.DO_NOTHING)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=40)  # Field name made lowercase.
    serveraorb = models.CharField(db_column='serverAorB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ups_ip = models.IntegerField(db_column='UPS_ip', blank=True, null=True)  # Field name made lowercase.
    ups_op = models.IntegerField(db_column='UPS_op', blank=True, null=True)  # Field name made lowercase.
    dust_free = models.CharField(db_column='Dust_free', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lan_status = models.CharField(db_column='LAN_status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    time_sync = models.CharField(max_length=5, blank=True, null=True)
    audio_quality = models.CharField(db_column='Audio_quality', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ptt_off_interval_seconds = models.IntegerField(blank=True, null=True)
    main_to_standby_changeover = models.CharField(max_length=5, blank=True, null=True)
    status_of_rop = models.CharField(db_column='status_of_ROP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datisweekly'
        unique_together = (('date', 'a'),)


class Datiswlogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING)
    p = models.ForeignKey(Datisweekly, models.DO_NOTHING)
    remarks = models.CharField(db_column='Remarks', max_length=100)  # Field name made lowercase.
    value = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'datiswlogs'


class Dgm(models.Model):
    dgm_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    designation = models.CharField(max_length=10, blank=True, null=True)
    a = models.ForeignKey(Airport, models.DO_NOTHING, blank=True,related_name='ok', null=True)
    contact = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    head = models.ForeignKey('Head', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'dgm'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class DgmReports(models.Model):
    r_id = models.IntegerField(primary_key=True)
    r_type = models.CharField(max_length=30)
    r_status = models.CharField(max_length=30)
    r_count = models.PositiveIntegerField()
    r_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dgmreports'

class Dmedaily(models.Model):
    date = models.DateTimeField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    f_id = models.CharField(max_length=10)
    eqpt_shelter_cleanliness = models.CharField(max_length=10, blank=True, null=True)
    battery_room_cleanliness = models.CharField(db_column='Battery_room_cleanliness', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ac_status = models.CharField(db_column='AC_status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    eqpt_shelter_temperature = models.FloatField(blank=True, null=True)
    mains_power_supply = models.IntegerField(blank=True, null=True)
    stabiliser_output = models.IntegerField(blank=True, null=True)
    batterybank_voltage = models.IntegerField(blank=True, null=True)
    status_of_monitor = models.CharField(max_length=10, blank=True, null=True)
    unusual_noise = models.CharField(max_length=10, blank=True, null=True)
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    p_id = models.IntegerField(primary_key=True)
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'dmedaily'
        unique_together = (('date', 'a'),)


class Dmemonthly(models.Model):
    date = models.DateTimeField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    f_id = models.CharField(max_length=10)
    sgdnf_pulse_width = models.FloatField(db_column='SGDNF_pulse_width', blank=True, null=True)  # Field name made lowercase.
    sgdnf_amplitude = models.FloatField(db_column='SGDNF_amplitude', blank=True, null=True)  # Field name made lowercase.
    squitter_rate_of_inhibit_interrogation = models.FloatField(db_column='Squitter_rate_of_inhibit_interrogation', blank=True, null=True)  # Field name made lowercase.
    max_reply_rate_khz = models.FloatField(db_column='max_reply_rate_KHz', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    p_id = models.IntegerField(primary_key=True)
    s_verify = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30)
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmemonthly'
        unique_together = (('date', 'a'),)


class Dmeweekly(models.Model):
    date = models.DateTimeField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    f_id = models.CharField(max_length=10)
    test_interrogation_module = models.IntegerField(blank=True, null=True)
    rx_video_module = models.IntegerField(db_column='RX_video_module', blank=True, null=True)  # Field name made lowercase.
    number_100w_module = models.IntegerField(db_column='100W_module', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    monitor_module = models.IntegerField(db_column='Monitor_module', blank=True, null=True)  # Field name made lowercase.
    ac_regulator_ip = models.IntegerField(db_column='AC_regulator_ip', blank=True, null=True)  # Field name made lowercase.
    ac_regulator_op = models.IntegerField(db_column='AC_regulator_op', blank=True, null=True)  # Field name made lowercase.
    system_delay = models.FloatField(blank=True, null=True)
    pulse_pair_spacing_sepn = models.FloatField(db_column='pulse_pair_spacing_SEPN', blank=True, null=True)  # Field name made lowercase.
    reply_efficiency_percent = models.FloatField(blank=True, null=True)
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    p_id = models.AutoField(primary_key=True)
    s_verify = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30)
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmeweekly'
        unique_together = (('date', 'a'),)


class Dscndaily(models.Model):
    p_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    f = models.ForeignKey(Communication, models.DO_NOTHING)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    sat_led = models.CharField(db_column='SAT_LED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odu_led = models.CharField(db_column='ODU_LED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    io_led = models.CharField(db_column='IO_LED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    alarm_led = models.CharField(db_column='Alarm_LED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    power_led = models.CharField(db_column='Power_LED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    v35_led = models.CharField(db_column='V35_LED', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ip_voltage = models.IntegerField(db_column='IP_Voltage', blank=True, null=True)  # Field name made lowercase.
    op_voltage = models.IntegerField(db_column='OP_voltage', blank=True, null=True)  # Field name made lowercase.
    battery_voltage = models.IntegerField(db_column='Battery_Voltage', blank=True, null=True)  # Field name made lowercase.
    coro_function = models.CharField(db_column='CorO_function', max_length=5, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dscndaily'
        unique_together = (('date', 'a'),)


class Dscndlogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING)
    remarks = models.CharField(max_length=100)
    value = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    p = models.ForeignKey(Dscndaily, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dscndlogs'


class Dscnmonthly(models.Model):
    p_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    f_id = models.IntegerField(blank=True, null=True)
    cleaning_dscn_associated_eqpt = models.TextField(db_column='Cleaning_DSCN_associated_eqpt', blank=True, null=True)  # Field name made lowercase.
    battery_backup_time_of_ups1nups2 = models.TextField(db_column='Battery_backup_time_of_UPS1nUPS2', blank=True, null=True)  # Field name made lowercase.
    ups_battery_voltage_on_load = models.TextField(db_column='UPS_battery_voltage_on_load', blank=True, null=True)  # Field name made lowercase.
    antenna_n_cable_check = models.TextField(db_column='Antenna_n_cable_check', blank=True, null=True)  # Field name made lowercase.
    earth_resistance = models.TextField(db_column='Earth_resistance', blank=True, null=True)  # Field name made lowercase.
    eorn_voltage = models.IntegerField(db_column='EorN_voltage', blank=True, null=True)  # Field name made lowercase.
    eqpt_status_after_check = models.CharField(max_length=5, blank=True, null=True)
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=30)
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dscnmonthly'
        unique_together = (('date', 'a'),)

class Dscnmlogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING)
    remarks = models.CharField(max_length=100)
    value = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    p = models.ForeignKey(Dscnmonthly, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dscnmlogs'

class Dscnweekly(models.Model):
    p_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    f = models.ForeignKey(Communication, models.DO_NOTHING)
    air_conditioning_check = models.TextField(db_column='Air_conditioning_check', blank=True, null=True)  # Field name made lowercase.
    cleaning_dscn_associated_eqpt = models.TextField(db_column='Cleaning_DSCN_associated_eqpt', blank=True, null=True)  # Field name made lowercase.
    ups1_ups2_battery_backup = models.TextField(db_column='UPS1_UPS2_battery_backup', blank=True, null=True)  # Field name made lowercase.
    ups_battery_voltage_on_load = models.TextField(db_column='UPS_battery_voltage_on_load', blank=True, null=True)  # Field name made lowercase.
    antenna_n_cable_check = models.TextField(db_column='Antenna_n_Cable_check', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'dscnweekly'
        unique_together = (('date', 'a'),)

class Dscnwlogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING)
    remarks = models.CharField(max_length=100)
    value = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    p = models.ForeignKey(Dscnweekly, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dscnwlogs'

class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=10)
    a = models.ForeignKey(Airport, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee'


class Engineer(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    designation = models.CharField(max_length=10, blank=True, null=True)
    a = models.ForeignKey(Airport, models.DO_NOTHING, blank=True, null=True)
    dept = models.CharField(max_length=1, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    supervisor = models.ForeignKey('Supervisor', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'engineer'


class Head(models.Model):
    head_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    designation = models.CharField(max_length=10, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'head'


class Issues(models.Model):
    issue_no = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey(Engineer, models.DO_NOTHING, blank=True, null=True)
    topic = models.CharField(db_column='Topic', max_length=30)  # Field name made lowercase.
    desgn = models.CharField(max_length=10, blank=True, null=True)
    dept = models.CharField(max_length=1, blank=True, null=True)
    facility_affected = models.CharField(max_length=20, blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    actions_taken = models.TextField(blank=True, null=True)
    approved_by = models.ForeignKey(Employee, models.DO_NOTHING, db_column='approved_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issues'
        unique_together = (('issue_no', 'date', 'a'), ('issue_no', 'a'),)


class Mcdo(models.Model):
    emp = models.OneToOneField(Employee, models.DO_NOTHING, primary_key=True)
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    topic = models.CharField(max_length=50)
    dop = models.DateTimeField(db_column='DOP')  # Field name made lowercase.
    content = models.TextField()
    doa = models.DateTimeField(db_column='DOA', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.ForeignKey(Employee, models.DO_NOTHING, db_column='approved_by',related_name='b', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mcdo'
        unique_together = (('emp', 'a'),)


class Navigation(models.Model):
    f_id = models.CharField(primary_key=True, max_length=10)
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    facility = models.CharField(max_length=20, blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    idnt = models.CharField(db_column='IDNT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    coordinaten = models.CharField(db_column='coordinateN', max_length=11, blank=True, null=True)  # Field name made lowercase.
    coordinatee = models.CharField(db_column='coordinateE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    eqpt = models.CharField(max_length=20, blank=True, null=True)
    doi = models.DateField(db_column='DOI', blank=True, null=True)  # Field name made lowercase.
    doc = models.DateField(db_column='DOC', blank=True, null=True)  # Field name made lowercase.
    supervisor = models.ForeignKey('Supervisor', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'navigation'
        unique_together = (('f_id', 'a'), ('f_id', 'a'),)


class Ndbdaily(models.Model):
    date = models.DateTimeField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey(Engineer, models.DO_NOTHING, blank=True, null=True)
    f_id = models.CharField(max_length=10)
    room_temp = models.IntegerField(blank=True, null=True)
    ac_mains_voltage_50hz = models.IntegerField(db_column='ac_mains_voltage_50Hz', blank=True, null=True)  # Field name made lowercase.
    battery_voltage = models.IntegerField(blank=True, null=True)
    reflected_power = models.IntegerField(blank=True, null=True)
    forward_power = models.IntegerField(blank=True, null=True)
    modulation = models.IntegerField(blank=True, null=True)
    system_status_led = models.CharField(db_column='system_status_LED', max_length=3, blank=True, null=True)  # Field name made lowercase.
    primary_tx_led = models.CharField(db_column='Primary_TX_LED', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tx_power_on_led = models.CharField(db_column='TX_power_ON_LED', max_length=3, blank=True, null=True)  # Field name made lowercase.
    remote_ctrl_link_led = models.CharField(db_column='remote_ctrl_link_LED', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)
    s_verify = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ndbdaily'
        unique_together = (('date', 'a'),)


class Ndbmonthly(models.Model):
    date = models.DateTimeField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey(Engineer, models.DO_NOTHING, blank=True, null=True)
    f_id = models.CharField(max_length=10)
    frwd_power_modulation_off = models.IntegerField(db_column='frwd_power_modulation_OFF', blank=True, null=True)  # Field name made lowercase.
    reflected_power = models.IntegerField(blank=True, null=True)
    modulation_depth_check = models.IntegerField(blank=True, null=True)
    ident_code_check = models.CharField(max_length=10, blank=True, null=True)
    antenna_n_acu_check = models.CharField(db_column='antenna_n_ACU_check', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ndb_eqpt_n_acu_cleaning = models.CharField(db_column='NDB_eqpt_n_ACU_cleaning', max_length=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)
    s_verify = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ndbmonthly'
        unique_together = (('date', 'a'),)


class Ndbweekly(models.Model):
    date = models.DateTimeField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey(Engineer, models.DO_NOTHING, blank=True, null=True)
    f_id = models.CharField(max_length=10)
    mains_pwr_supply_check = models.TextField(blank=True, null=True)
    battery_terminals_check = models.TextField(blank=True, null=True)
    battery_sealed = models.CharField(max_length=3, blank=True, null=True)
    specific_gravity = models.FloatField(blank=True, null=True)
    antenna_site_condition = models.TextField(blank=True, null=True)
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)
    s_verify = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ndbweekly'
        unique_together = (('date', 'a'),)


class Scctvdaily(models.Model):
    date = models.DateField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    f_id = models.CharField(max_length=10)
    ups_battery_indication = models.CharField(db_column='UPS_battery_indication', max_length=20, blank=True, null=True)  # Field name made lowercase.
    servers_on_condition = models.CharField(db_column='Servers_ON_condition', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nas_status_in_vmsorvrm = models.CharField(db_column='NAS_status_in_VMSorVRM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    recording_active_status_vrs_server = models.CharField(db_column='recording_active_status_VRS_server', max_length=11, blank=True, null=True)  # Field name made lowercase.
    recording_active_status_rrs_server = models.CharField(db_column='recording_active_status_RRS_server', max_length=20, blank=True, null=True)  # Field name made lowercase.
    database_status_vms = models.CharField(db_column='database_status_VMS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cameras_ivms = models.CharField(db_column='cameras_IVMS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    eqpt_cleaning = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=30)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scctvdaily'


class Scctvdlogs(models.Model):
    emp = models.ForeignKey(Engineer, models.DO_NOTHING)
    value = models.CharField(max_length=30)
    remarks = models.CharField(max_length=30)
    log_id = models.AutoField(primary_key=True)
    p = models.ForeignKey(Scctvdaily, models.DO_NOTHING)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scctvdlogs'


class Scctvmonthly(models.Model):
    date = models.DateField()
    time = models.TimeField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey(Engineer, models.DO_NOTHING, blank=True, null=True)
    f_id = models.CharField(max_length=10)
    ups_ip_voltage = models.IntegerField(blank=True, null=True)
    ups_op_voltage = models.IntegerField(blank=True, null=True)
    ups_battery_op_voltage_acpwron = models.IntegerField(db_column='ups_battery_op_voltage_ACpwrON', blank=True, null=True)  # Field name made lowercase.
    ups_battery_op_voltage_acpwroff = models.IntegerField(db_column='ups_battery_op_voltage_ACpwrOFF', blank=True, null=True)  # Field name made lowercase.
    ups_battery_op_voltage_after15min_acpwroff = models.IntegerField(db_column='ups_battery_op_voltage_after15min_ACpwrOFF', blank=True, null=True)  # Field name made lowercase.
    server_status = models.CharField(max_length=5, blank=True, null=True)
    cameras_in_vrs_server = models.CharField(db_column='cameras_in_VRS_server', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nas_free_capacity = models.FloatField(db_column='NAS_free_capacity', blank=True, null=True)  # Field name made lowercase.
    ofclinkto_l2l3_switches = models.CharField(db_column='OFClinkto_L2L3_switches', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cleaning_camera_eqpt = models.CharField(max_length=20, blank=True, null=True)
    user_rights_check = models.CharField(max_length=10, blank=True, null=True)
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'scctvmonthly'
        unique_together = (('date', 'a'),)

class Scctvmlogs(models.Model):
    emp = models.ForeignKey(Engineer, models.DO_NOTHING)
    value = models.CharField(max_length=30)
    remarks = models.CharField(max_length=30)
    log_id = models.AutoField(primary_key=True)
    p = models.ForeignKey(Scctvmonthly, models.DO_NOTHING)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scctvmlogs'

class Scctvweekly(models.Model):
    date = models.DateField()
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    emp = models.ForeignKey(Engineer, models.DO_NOTHING, blank=True, null=True)
    f_id = models.CharField(max_length=10)
    ups_ip_voltage = models.IntegerField(blank=True, null=True)
    ups_op_voltage = models.IntegerField(blank=True, null=True)
    ups_battery_status = models.CharField(max_length=10, blank=True, null=True)
    server_status = models.CharField(max_length=5, blank=True, null=True)
    camera_nas_status_in_vrs = models.CharField(db_column='camera_NAS_status_in_VRS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    workstns_n_client_softw_check = models.CharField(max_length=10, blank=True, null=True)
    cameras_client_ivms_softw = models.CharField(db_column='cameras_client_IVMS_softw', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nas_free_capacity = models.FloatField(db_column='NAS_free_capacity', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=30)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scctvweekly'


class Scctvwlogs(models.Model):
    p = models.ForeignKey(Scctvweekly, models.DO_NOTHING)
    log_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    value = models.CharField(max_length=30)
    remarks = models.CharField(max_length=30)
    emp = models.ForeignKey(Engineer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'scctvwlogs'


class Supervisor(models.Model):
    supervisor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    designation = models.CharField(max_length=10, blank=True, null=True)
    a = models.ForeignKey(Airport, models.DO_NOTHING, blank=True, null=True)
    dept = models.CharField(max_length=1, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    dgm = models.ForeignKey(Dgm, models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'supervisor'


class Surveillance(models.Model):
    f_id = models.IntegerField(primary_key=True)
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    facility = models.CharField(max_length=20, blank=True, null=True)
    eqpt = models.CharField(max_length=20, blank=True, null=True)
    doi = models.DateField(db_column='DOI', blank=True, null=True)  # Field name made lowercase.
    doc = models.DateField(db_column='DOC', blank=True, null=True)  # Field name made lowercase.
    supervisor = models.ForeignKey(Supervisor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surveillance'
        unique_together = (('f_id', 'a'), ('f_id', 'a'),)


class Vhfdaily(models.Model):
    p_id = models.AutoField(primary_key=True)
    s_verify = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    emp = models.ForeignKey(Engineer, models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=40)
    f = models.ForeignKey(Communication, models.DO_NOTHING)
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    rx_no = models.IntegerField(db_column='RX_no', blank=True, null=True)  # Field name made lowercase.
    frequency_mhz = models.IntegerField(db_column='frequency_MHz', blank=True, null=True)  # Field name made lowercase.
    bit_test = models.CharField(max_length=10, blank=True, null=True)
    vstatus = models.CharField(max_length=10, blank=True, null=True)
    rxn_check = models.CharField(db_column='RXN_check', max_length=10, blank=True, null=True)  # Field name made lowercase.
    acordc_coro = models.CharField(db_column='ACorDC_CorO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sq_threshold = models.IntegerField(db_column='SQ_threshold', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_Incharge_Approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vhfdaily'
        unique_together = (('date', 'a'),)


class Vhfdlogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Engineer, models.DO_NOTHING)
    remarks = models.CharField(max_length=100)
    value = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    p = models.ForeignKey(Vhfdaily, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vhfdlogs'


class Vhfmlogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp_id = models.IntegerField()
    value = models.CharField(max_length=30)
    remarks = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'vhfmlogs'


class Vhfmonthly(models.Model):
    p_id = models.AutoField(primary_key=True)
    date = models.DateField(unique=True)
    time = models.TimeField()
    emp = models.ForeignKey(Engineer, models.DO_NOTHING, blank=True, null=True)
    f = models.ForeignKey(Communication, models.DO_NOTHING)
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    modulation_mode = models.CharField(max_length=10, blank=True, null=True)
    line_op = models.IntegerField(blank=True, null=True)
    squelch_defeat = models.CharField(max_length=3, blank=True, null=True)
    squelch_threshold = models.IntegerField(blank=True, null=True)
    squelch_carrier_override = models.CharField(max_length=3, blank=True, null=True)
    rf_pre_attn = models.CharField(db_column='RF_pre_ATTN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    agc = models.CharField(db_column='AGC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ready_signal = models.CharField(db_column='Ready_signal', max_length=5, blank=True, null=True)  # Field name made lowercase.
    squelch_op_marc = models.CharField(db_column='Squelch_op_marc', max_length=5, blank=True, null=True)  # Field name made lowercase.
    squelch_op_facilities = models.CharField(db_column='Squelch_op_facilities', max_length=5, blank=True, null=True)  # Field name made lowercase.
    squelch_op_phantom = models.CharField(db_column='Squelch_op_phantom', max_length=5, blank=True, null=True)  # Field name made lowercase.
    squelch_defeat_ip = models.CharField(db_column='Squelch_defeat_ip', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bit_test = models.CharField(max_length=10, blank=True, null=True)
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)
    s_verify = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'vhfmonthly'
        unique_together = (('date', 'a'),)


class Vhfyearly(models.Model):
    p_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    emp = models.ForeignKey(Engineer, models.DO_NOTHING, blank=True, null=True)
    f = models.ForeignKey(Communication, models.DO_NOTHING)
    a = models.ForeignKey(Airport, models.DO_NOTHING)
    rx_no = models.IntegerField(db_column='RX_no', blank=True, null=True)  # Field name made lowercase.
    frequency_mhz = models.FloatField(db_column='frequency_MHz', blank=True, null=True)  # Field name made lowercase.
    reference_freq = models.FloatField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    bit_test = models.CharField(max_length=5, blank=True, null=True)
    ac_dc_changeover = models.CharField(db_column='AC_DC_changeover', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    unit_incharge_approval = models.CharField(db_column='Unit_incharge_approval', max_length=3, blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(blank=True, null=True)
    approval_time = models.TimeField(blank=True, null=True)
    s_verify = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'vhfyearly'
        unique_together = (('date', 'a'),)


class Vhfylogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Engineer, models.DO_NOTHING)
    remarks = models.CharField(max_length=100)
    value = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'vhfylogs'
