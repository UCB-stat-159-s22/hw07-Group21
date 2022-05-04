## PUMS Documentation

Sources: 
* [Documentation Website](https://www.census.gov/programs-surveys/acs/microdata/documentation.html)
* [Sample Dictionary of Codes](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2018.pdf) (from 2018) 



| Code Tag    | Code Name |  Notes/Values|
| ----------- | ----------- | ----------- |
| `AGEP`      |   Person Age     |    Age as `int`    |
| `SEX`      |    Sex    |   1 - Male, 2 - Female     |
| `SCHL`      |    Educational attainment    |    bb .N/A (less than 3 years old) <br> ... <br>16 .Regular high school diploma <br> 17 .GED or alternative credential <br> 18 .Some college, but less than 1 year <br> 19 .1 or more years of college credit, no degree <br> 20 .Associate's degree <br> 21 .Bachelor's degree <br> 22 .Master's degree <br> 23 .Professional degree beyond a bachelor's degree <br> 24 .Doctorate degree    |
| `WAGP`      |    Wages or salary income past 12 months (use ADJINC to adjust WAGP to constant dollars)    |    bbbbbb .N/A (less than 15 years old) <br>0 .None <br> 4..999999 .$4 to 999999 (Rounded and top-coded)    |
| `ADJINC`      |   Adjustment factor for income and earnings dollar amounts (6 implied decimal places)     |    1013097  => 1.013097 factor <br> only relevant for multi-year datasets  |
| `WKHP`      |   Usual hours worked per week past 12 months     |    bb N/A (less than 16 years old/did not work during the past 12 months) <br> 1..98 1 to 98 usual hours <br> 99 99 or more usual hours    |
| `WKW`      |    Weeks worked during past 12 months    |     b N/A (less than 16 years old/did not work during the past 12 months) <br> 1 50 to 52 weeks worked during past 12 months <br> 2 48 to 49 weeks worked during past 12 months <br> 3 40 to 47 weeks worked during past 12 months <br> 4 27 to 39 weeks worked during past 12 months <br> 5 14 to 26 weeks worked during past 12 months <br> 6 less than 14 weeks worked during past 12 months   |
| `FOD1P`      |   Recoded field of degree - first entry     |   See full list below     |
| `FOD2P`      |    Recoded field of degree - second entry    |    See full list below    |
| `PERNP`      |    Total person's earnings (use ADJINC to adjust to constant dollars)    |    bbbbbbb .N/A (less than 16 years old) <br> 0 .No earnings <br> -10000 .Loss of \\$ 10000 or more (Rounded \& bottom-coded <br> components) <br> -9999..-1 .Loss \\$ 1 to \\$ 9999 (Rounded components) <br> 1..1999998 \\$1 to \\$1999998 (Rounded & top-coded components)    |
| `CIT`      |    Citizenship status    |  1 Born in the U.S. <br> 2 Born in Puerto Rico, Guam, the U.S. Virgin Islands, or the Northern Marianas <br> 3 Born abroad of American parent(s) <br>4 U.S. citizen by naturalization <br>5 Not a citizen of the U.S.     |
| `COW`      |    Class of worker    |   b .N/A (less than 16 years old/NILF who last worked more than 5 years ago or never worked) <br> 1 .Employee of a private for-profit company or business, or of an individual, for wages, salary, or commissions <br>2 .Employee of a private not-for-profit, tax-exempt, or charitable organization <br> 3 .Local government employee (city, county, etc.) <br> 4 .State government employee <br> 5 .Federal government employee <br> 6 .Self-employed in own not incorporated business, professional practice, or farm <br> 7 .Self-employed in own incorporated business, professional practice or farm <br> 8 .Working without pay in family business or farm <br> 9 .Unemployed and last worked 5 years ago or earlier or never worked     |

### List of Degree Fields:

* **bbbb** - N/A (less than bachelor's degree)
* **1100** - General Agriculture
* **1101** - Agriculture Production And Management
* **1102** - Agricultural Economics
* **1103** - Animal Sciences
* **1104** - Food Science
* **1105** - Plant Science And Agronomy
* **1106** - Soil Science
* **1199** - Miscellaneous Agriculture
* **1301** - Environmental Science
* **1302** - Forestry
* **1303** - Natural Resources Management
* **1401** - Architecture
* **1501** - Area Ethnic And Civilization Studies
* **1901** - Communications
* **1902** - Journalism
* **1903** - Mass Media
* **1904** - Advertising And Public Relations
* **2001** - Communication Technologies
* **2100** - Computer And Information Systems
* **2101** - Computer Programming And Data Processing
* **2102** - Computer Science
* **2105** - Information Sciences
* **2106** - Computer Administration Management And Security
* **2107** - Computer Networking And Telecommunications
* **2201** - Cosmetology Services And Culinary Arts
* **2300** - General Education
* **2301** - Educational Administration And Supervision
* **2303** - School Student Counseling
* **2304** - Elementary Education
* **2305** - Mathematics Teacher Education
* **2306** - Physical And Health Education Teaching
* **2307** - Early Childhood Education
* **2308** - Science And Computer Teacher Education
* **2309** - Secondary Teacher Education
* **2310** - Special Needs Education
* **2311** - Social Science Or History Teacher Education
* **2312** - Teacher Education: Multiple Levels
* **2313** - Language And Drama Education
* **2314** - Art And Music Education
* **2399** - Miscellaneous Education
* **2400** - General Engineering
* **2401** - Aerospace Engineering
* **2402** - Biological Engineering
* **2403** - Architectural Engineering
* **2404** - Biomedical Engineering
* **2405** - Chemical Engineering
* **2406** - Civil Engineering
* **2407** - Computer Engineering
* **2408** - Electrical Engineering
* **2409** - Engineering Mechanics Physics And Science
* **2410** - Environmental Engineering
* **2411** - Geological And Geophysical Engineering
* **2412** - Industrial And Manufacturing Engineering
* **2413** - Materials Engineering And Materials Science
* **2414** - Mechanical Engineering
* **2415** - Metallurgical Engineering
* **2416** - Mining And Mineral Engineering
* **2417** - Naval Architecture And Marine Engineering
* **2418** - Nuclear Engineering
* **2419** - Petroleum Engineering
* **2499** - Miscellaneous Engineering
* **2500** - Engineering Technologies
* **2501** - Engineering And Industrial Management
* **2502** - Electrical Engineering Technology
* **2503** - Industrial Production Technologies
* **2504** - Mechanical Engineering Related Technologies
* **2599** - Miscellaneous Engineering Technologies
* **2601** - Linguistics And Comparative Language And Literature
* **2602** - French German Latin And Other Common Foreign Language Studies
* **2603** - Other Foreign Languages
* **2901** - Family And Consumer Sciences
* **3201** - Court Reporting
* **3202** - Pre-Law And Legal Studies
* **3301** - English Language And Literature
* **3302** - Composition And Rhetoric
* **3401** - Liberal Arts
* **3402** - Humanities
* **3501** - Library Science
* **3600** - Biology
* **3601** - Biochemical Sciences
* **3602** - Botany
* **3603** - Molecular Biology
* **3604** - Ecology
* **3605** - Genetics
* **3606** - Microbiology
* **3607** - Pharmacology
* **3608** - Physiology
* **3609** - Zoology
* **3611** - Neuroscience
* **3699** - Miscellaneous Biology
* **3700** - Mathematics
* **3701** - Applied Mathematics
* **3702** - Statistics And Decision Science
* **3801** - Military Technologies
* **4000** - Multi/Interdisciplinary Studies
* **4001** - Intercultural And International Studies
* **4002** - Nutrition Sciences
* **4005** - Mathematics And Computer Science
* **4006** - Cognitive Science And Biopsychology
* **4007** - Interdisciplinary Social Sciences
* **4101** - Physical Fitness Parks Recreation And Leisure
* **4801** - Philosophy And Religious Studies
* **4901** - Theology And Religious Vocations
* **5000** - Physical Sciences
* **5001** - Astronomy And Astrophysics
* **5002** - Atmospheric Sciences And Meteorology
* **5003** - Chemistry
* **5004** - Geology And Earth Science
* **5005** - Geosciences
* **5006** - Oceanography
* **5007** - Physics
* **5008** - Materials Science
* **5098** - Multi-Disciplinary Or General Science
* **5102** - Nuclear, Industrial Radiology, And Biological Technologies
* **5200** - Psychology
* **5201** - Educational Psychology
* **5202** - Clinical Psychology
* **5203** - Counseling Psychology
* **5205** - Industrial And Organizational Psychology
* **5206** - Social Psychology
* **5299** - Miscellaneous Psychology
* **5301** - Criminal Justice And Fire Protection
* **5401** - Public Administration
* **5402** - Public Policy
* **5403** - Human Services And Community Organization
* **5404** - Social Work
* **5500** - General Social Sciences
* **5501** - Economics
* **5502** - Anthropology And Archeology
* **5503** - Criminology
* **5504** - Geography
* **5505** - International Relations
* **5506** - Political Science And Government
* **5507** - Sociology
* **5599** - Miscellaneous Social Sciences
* **5601** - Construction Services
* **5701** - Electrical, Mechanical, And Precision Technologies And Production
* **5901** - Transportation Sciences And Technologies
* **6000** - Fine Arts
* **6001** - Drama And Theater Arts
* **6002** - Music
* **6003** - Visual And Performing Arts
* **6004** - Commercial Art And Graphic Design
* **6005** - Film Video And Photographic Arts
* **6006** - Art History And Criticism
* **6007** - Studio Arts
* **6099** - Miscellaneous Fine Arts
* **6100** - General Medical And Health Services
* **6102** - Communication Disorders Sciences And Services
* **6103** - Health And Medical Administrative Services
* **6104** - Medical Assisting Services
* **6105** - Medical Technologies Technicians
* **6106** - Health And Medical Preparatory Programs
* **6107** - Nursing
* **6108** - Pharmacy Pharmaceutical Sciences And Administration
* **6109** - Treatment Therapy Professions
* **6110** - Community And Public Health
* **6199** - Miscellaneous Health Medical Professions
* **6200** - General Business
* **6201** - Accounting
* **6202** - Actuarial Science
* **6203** - Business Management And Administration
* **6204** - Operations Logistics And E-Commerce
* **6205** - Business Economics
* **6206** - Marketing And Marketing Research
* **6207** - Finance
* **6209** - Human Resources And Personnel Management
* **6210** - International Business
* **6211** - Hospitality Management
* **6212** - Management Information Systems And Statistics
* **6299** - Miscellaneous Business & Medical Administration
* **6402** - History
* **6403** - United States History
