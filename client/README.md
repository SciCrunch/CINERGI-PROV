post_client.py: python post_client.py <filename>


&nbsp;&nbsp;&nbsp; POST /gprov/api/v2.0/provenance/resource/	


&nbsp;&nbsp;&nbsp; Post PROV-DM compliant provenance of a ‘uuid’ labeled resource/entity.

q1_client.py: python q1_client.py -u <uuid>


&nbsp;&nbsp;&nbsp; GET /gprov/api/v2.0/provenance/b/resource/:id	


&nbsp;&nbsp;&nbsp; Retrieve PROV-DM compliant backward provenance about the resource with the given ‘uuid’.	

q2_client.py: python q2_client.py -u <uuid> -a <activity_property>


&nbsp;&nbsp;&nbsp; GET /gprov/api/v2.0/provenance/b/resource/:id/activity/:activity property/ 	


&nbsp;&nbsp;&nbsp; Retrieve PROV-DM compliant backward provenance  of a resource with a given ‘uuid’, and which has activity ‘activityname’ in its path  

q3_client.py: python q3_client.py -d <direction> -p <resource property>


&nbsp;&nbsp;&nbsp; GET /gprov/api/v2.0/provenance/:direction/resource/:resource property


&nbsp;&nbsp;&nbsp; Retrieve PROV-DM compliant 'direction' provenance  of a resource with a given property

q5_client.py: python q5_client.py -d <direction> -p <resource property>


&nbsp;&nbsp;&nbsp; GET /gprov/api/v2.0/provenance/:direction/resource/:resource property/activity/:activity property/	


&nbsp;&nbsp;&nbsp; Retrieve PROV-DM compliant provenance  of a resource with a given property, which has activity ‘activity prop’ in its 'direction' path

q7_client.py: python q7_client.py -d <direction> -a <activity property> -t1 <time1> -t2 <time2>


&nbsp;&nbsp;&nbsp; GET /gprov/api/v2.0/provenance/:direction/activity/:activity name/from/:datetime1/to/:datetime2/	


&nbsp;&nbsp;&nbsp; Retrieve PROV-DM compliant 'direction' provenance  of all resources used by an activity ‘activity name’ from time ‘dateime1’ to ‘datetime2’

