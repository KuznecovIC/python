from marvel import full_dict

user_nums = list(map(lambda x: int(x) if x.isdigit() else None, input("Enter your numbers:").split()))

filtered_dict = {id: data for id, data in full_dict.items() if id in user_nums}

directors_set = {data['director'] for data in filtered_dict.values()}

yesr_dict = {id: {**data, "year": str(data['year'])} for id, data in full_dict.items()}

sorted_films = dict(sorted(filtered_dict.items(), key=lambda x: (x[1]['year'], x[1]['title'])))