countries_to_remove = [
    'Marshall Islands', 'Cook Islands', 'Dominica', 'Monaco', 
    'Nauru', 'Niue', 'Saint Kitts and Nevis', 'San Marino', 
    'Tuvalu', 'Palau'
]

percentile_impute_columns = ['Alcohol', 'Hepatitis_B', 'Total_expenditure', 'GDP', 'Population']

median_impute_columns = ['BMI', 'Polio', 'Diphtheria', 'Thinness_ten_nineteen_years', 'Thinness_five_nine_years', 'Income_composition_of_resources', 'Schooling']

outliers_left_columns = ['Life_expectancy','Polio','Diphtheria','Income_composition_of_resources', 'Schooling']

outliers_right_columns = [ 'Adult_Mortality', 'Infant_deaths', 'Alcohol','Percentage_expenditure', 'Measles', 'Under_five_deaths','Total_expenditure','Incidents_HIV', 'GDP', 'Population', 'Thinness_ten_nineteen_years', 'Thinness_five_nine_years','Schooling']

country_to_region = {
    'Cabo Verde': 'Africa', 'Saint Lucia': 'North America', 'Tunisia': 'Africa', 'Brunei Darussalam': 'Asia',
    'Equatorial Guinea': 'Africa', 'Papua New Guinea': 'Oceania', 'Ecuador': 'South America', 'Mongolia': 'Asia',
    'Poland': 'Europe', 'Oman': 'Asia', 'Senegal': 'Africa', 'Kuwait': 'Asia', 'Sierra Leone': 'Africa',
    'Saudi Arabia': 'Asia', 'India': 'Asia', 'Chad': 'Africa', 'Guinea-Bissau': 'Africa', 'Mauritius': 'Africa',
    'Ghana': 'Africa', 'Solomon Islands': 'Oceania', 'Ireland': 'Europe', 'Israel': 'Asia', 'Fiji': 'Oceania',
    'Uzbekistan': 'Asia', 'France': 'Europe', 'Malaysia': 'Asia', 'Singapore': 'Asia', "Côte d'Ivoire": 'Africa',
    'El Salvador': 'North America', 'Belarus': 'Europe', 'Luxembourg': 'Europe', 'Armenia': 'Asia', 'Turkmenistan': 'Asia',
    'Bahamas': 'North America', 'Belgium': 'Europe', 'Nicaragua': 'North America', 'Lesotho': 'Africa',
    'Iran (Islamic Republic of)': 'Asia', 'Dominican Republic': 'North America', 'Liberia': 'Africa',
    'Serbia': 'Europe', 'Denmark': 'Europe', 'Netherlands': 'Europe', 'Kyrgyzstan': 'Asia', 'Slovenia': 'Europe',
    'Kazakhstan': 'Asia', 'Azerbaijan': 'Asia', 'Nepal': 'Asia', 'Montenegro': 'Europe',
    'Democratic Republic of the Congo': 'Africa', 'Mali': 'Africa',
    'United Kingdom of Great Britain and Northern Ireland': 'Europe', 'Bolivia (Plurinational State of)': 'South America', 
    'South Sudan': 'Africa', 'Finland': 'Europe', 'Cyprus': 'Europe', 'Uruguay': 'South America', 'Belize': 'North America',
    'United Republic of Tanzania': 'Africa', 'Madagascar': 'Africa', "Lao People's Democratic Republic": 'Asia',
    'Bahrain': 'Asia', 'Ukraine': 'Europe', 'Sweden': 'Europe', 'Kenya': 'Africa', 'Micronesia (Federated States of)': 'Oceania',
    'Cuba': 'North America', 'Cameroon': 'Africa', 'Gambia': 'Africa', 'Somalia': 'Africa', 'Pakistan': 'Asia', 'Malawi': 'Africa',
    'Yemen': 'Asia', 'Tajikistan': 'Asia', 'Mozambique': 'Africa', 'Jamaica': 'North America', 'Namibia': 'Africa', 'Spain': 'Europe',
    'Tonga': 'Oceania', 'Peru': 'South America', 'Botswana': 'Africa', 'Mexico': 'North America', 'Sao Tome and Principe': 'Africa',
    'Croatia': 'Europe', 'Malta': 'Europe', 'Switzerland': 'Europe', 'Honduras': 'North America',
    'Venezuela (Bolivarian Republic of)': 'South America', 'Uganda': 'Africa', 'Congo': 'Africa', 'Germany': 'Europe',
    'Georgia': 'Asia', 'Norway': 'Europe', 'Swaziland': 'Africa', 'Chile': 'South America', 'Slovakia': 'Europe', 'Iceland': 'Europe',
    'Brazil': 'South America', 'Barbados': 'North America', 'Myanmar': 'Asia', 'Guatemala': 'North America', 'Marshall Islands': 'Oceania',
    'Angola': 'Africa', 'Mauritania': 'Africa', 'China': 'Asia', 'Seychelles': 'Africa', 'Eritrea': 'Africa',
    'Morocco': 'Africa', "Democratic People's Republic of Korea": 'Asia', 'Burundi': 'Africa',
    'Antigua and Barbuda': 'North America', 'Timor-Leste': 'Asia', 'Djibouti': 'Africa', 'Romania': 'Europe',
    'Nigeria': 'Africa', 'Benin': 'Africa', 'The former Yugoslav republic of Macedonia': 'Europe',
    'Egypt': 'Africa', 'Comoros': 'Africa', 'Zimbabwe': 'Africa', 'Trinidad and Tobago': 'North America', 'Canada': 'North America',
    'Central African Republic': 'Africa', 'Lithuania': 'Europe', 'Sudan': 'Africa', 'Costa Rica': 'North America',
    'Republic of Moldova': 'Europe', 'Lebanon': 'Asia', 'Qatar': 'Asia', 'Sri Lanka': 'Asia',
    'United Arab Emirates': 'Asia', 'Indonesia': 'Asia', 'Saint Vincent and the Grenadines': 'North America', 'Panama': 'North America',
    'Albania': 'Europe', 'Paraguay': 'South America', 'Rwanda': 'Africa', 'Republic of Korea': 'Asia', 'Haiti': 'North America', 'Iraq': 'Asia',
    'Bhutan': 'Asia', 'Colombia': 'South America', 'Turkey': 'Asia', 'Philippines': 'Asia', 'Guinea': 'Africa', 'Grenada': 'North America',
    'Maldives': 'Asia', 'Gabon': 'Africa', 'New Zealand': 'Oceania', 'Samoa': 'Oceania', 'South Africa': 'Africa',
    'Niue': 'Oceania', 'Latvia': 'Europe', 'Australia': 'Oceania', 'Burkina Faso': 'Africa', 'Libya': 'Africa',
    'Bosnia and Herzegovina': 'Europe', 'Kiribati': 'Oceania', 'Argentina': 'South America', 'Cambodia': 'Asia',
    'Vanuatu': 'Oceania', 'Zambia': 'Africa', 'Japan': 'Asia', 'Guyana': 'South America', 'Afghanistan': 'Asia', 'Suriname': 'South America',
    'Thailand': 'Asia', 'Bangladesh': 'Asia', 'Greece': 'Europe', 'Austria': 'Europe', 'Ethiopia': 'Africa', 'Togo': 'Africa',
    'Czechia': 'Europe', 'Niger': 'Africa', 'Italy': 'Europe', 'Hungary': 'Europe', 'Estonia': 'Europe', 'Viet Nam': 'Asia',
    'Jordan': 'Asia', 'Russian Federation': 'Europe', 'Syrian Arab Republic': 'Asia',
    'United States of America': 'North America', 'Portugal': 'Europe', 'Bulgaria': 'Europe',
    'Saint Kitts and Nevis': 'North America', 'Algeria': 'Africa', 'Nauru': 'Oceania', 'Cook Islands': 'Oceania',
    'Palau': 'Oceania', 'Monaco': 'Europe', 'Dominica': 'North America'
}

columns_encoding = ['Region', 'Status']

colmns_to_scale = ['Population', 'GDP', 'Percentage_expenditure', 'Total_expenditure']

X_column = ['Unnamed: 0', 'Year', 'Adult_Mortality', 'Alcohol',
       'Percentage_expenditure', 'Hepatitis_B', 'Measles', 'BMI',
       'Under_five_deaths', 'Polio', 'Total_expenditure', 'Diphtheria',
       'Incidents_HIV', 'GDP', 'Population', 'Thinness_ten_nineteen_years',
       'Thinness_five_nine_years', 'Income_composition_of_resources',
       'Schooling', 'Region_Africa', 'Region_Asia', 'Region_Europe',
       'Region_North America', 'Region_Oceania', 'Region_South America',
       'Status_Developed']

y_column = ['Life_expectancy']