#URL for round-trip to three European regions
regions_list = ['Western', 'Eastern', 'Southern']


rt_western_europe_url = {
	'front_url' : 'https://www.google.com/flights?hl=en#flt=/m/0rh6k.r/m/0852h.',
	'middle_url' : '*r/m/0852h./m/0rh6k.',
	'back_url' : ';c:USD;e:1;ls:1w;sd:1;t:e'
	}

rt_southern_europe_url = {
	'front_url' : 'https://www.google.com/flights?hl=en#flt=/m/0rh6k.r/m/0250wj.',
	'middle_url' : '*r/m/0250wj./m/0rh6k.',
	'back_url' : ';c:USD;e:1;ls:1w;sd:1;t:e'
	}

rt_eastern_europe_url = {
	'front_url' : 'https://www.google.com/flights?hl=en#flt=/m/0rh6k.r/m/09b69.',
	'middle_url' : '*r/m/09b69./m/0rh6k.',
	'back_url' : ';c:USD;e:1;ls:1w;sd:1;t:e'
	}

rt_regions_dict = {
	"Western" : rt_western_europe_url,
	"Southern" : rt_southern_europe_url,
	"Eastern" : rt_eastern_europe_url
	}


#ONE WAY URLS
"""First-part + variable_location + date + Back-part
			FIRST AND LAST PART ARE SAME FOR ALL"""

ow_western_europe_url = {
	'front_url' : 'https://www.google.com/flights?hl=en#flt=/m/0rh6k.r/m/',
	'middle_url' : '0852h.',
	'back_url' : ';c:USD;e:1;ls:1w;sd:1;t:e;tt:o'
	}

ow_southern_europe_url = {
	'front_url' : 'https://www.google.com/flights?hl=en#flt=/m/0rh6k.r/m/',
	'middle_url' : '0250wj.',
	'back_url' : ';c:USD;e:1;ls:1w;sd:1;t:e;tt:o'
	}

ow_eastern_europe_url = {
	'front_url' : 'https://www.google.com/flights?hl=en#flt=/m/0rh6k.r/m/',
	'middle_url' : '09b69.',
	'back_url' : ';c:USD;e:1;ls:1w;sd:1;t:e;tt:o'
	}

ow_regions_dict = {
	"Western" : ow_western_europe_url,
	"Southern" : ow_southern_europe_url,
	"Eastern" : ow_eastern_europe_url
	}


one_way_url_head = 'https://www.google.com/flights?hl=en#flt=/m/0rh6k.r/m/'
one_way_url_back = ';c:USD;e:1;ls:1w;sd:1;t:e;tt:o'

#TO WESTERN EUROPE
one_way_western_europe_url = '0852h.'
#TO EASTERN EUROPE
one_way_eastern_europe_url = '09b69.'
#TO SOUTHERN EUROPE
one_way_southern_europe_url = '0250wj.'




