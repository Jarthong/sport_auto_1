from db_fixture.getdata import GetData

__author__ = 'huxm855'


deviceType = range(2, 3)
version, versionName, = GetData('version,version_name', table='app_version', limt=1,
                                where="where device_type={device_type} order by create_time desc".format(
                                    device_type=deviceType)).result()
