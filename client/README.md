post_client.py: python post_client.py <filename>
	POST /gprov/api/v2.0/provenance/resource/	
	Post PROV-DM compliant provenance of a ‘uuid’ labeled resource/entity.

q1_client.py: python q1_client.py -u <uuid>
	GET /gprov/api/v2.0/provenance/b/resource/:id	
	Retrieve PROV-DM compliant backward provenance about the resource with the given ‘uuid’.	

q2_client.py: python q2_client.py -u <uuid> -a <activity_property>
	GET /gprov/api/v2.0/provenance/b/resource/:id/activity/:activity property/ 	
	Retrieve PROV-DM compliant backward provenance  of a resource with a given ‘uuid’, and which has activity ‘activityname’ in its path  

q3_client.py: python q3_client.py -d <direction> -p <resource property>
	GET /gprov/api/v2.0/provenance/:direction/resource/:resource property
	Retrieve PROV-DM compliant 'direction' provenance  of a resource with a given property

q5_client.py: python q5_client.py -d <direction> -p <resource property>
	GET /gprov/api/v2.0/provenance/:direction/resource/:resource property/activity/:activity property/	
	Retrieve PROV-DM compliant provenance  of a resource with a given property, which has activity ‘activity prop’ in its 'direction' path

q7_client.py: python q7_client.py -d <direction> -a <activity property> -t1 <time1> -t2 <time2>
	GET /gprov/api/v2.0/provenance/:direction/activity/:activity name/datetime/:datetime1/datetime/:datetime2/	
	Retrieve PROV-DM compliant 'direction' provenance  of all resources used by an activity ‘activity name’ between time ‘dateime1’ and ‘datetime2’

