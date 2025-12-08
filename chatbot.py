import re

class SchemeAssistant:
    def __init__(self):
        self.language = None  # 'en' or 'gu'

    def detect_language(self, text):
        # Simple detection: check for Gujarati unicode range
        for char in text:
            if '\u0a80' <= char <= '\u0aff':
                return 'gu'
        return 'en'

    def process_message(self, message):
        # Always detect language from the current message
        self.language = self.detect_language(message)
        
        # Identify topic
        topic = self.identify_topic(message)
        
        if topic:
            return self.get_scheme_info(topic)
        else:
            return self.get_out_of_scope_response()

    def identify_topic(self, text):
        text = text.lower()
        
        # Keywords mapping
        keywords = {
            'agriculture': ['farmer', 'crop', 'irrigation', 'fisheries', 'husbandry', 'khedut', 'ખેડૂત', 'પાક', 'સિંચાઈ', 'મત્સ્ય', 'પશુપાલન'],
            'women': ['women', 'girl', 'widow', 'anganwadi', 'nutrition', 'mahila', 'beti', 'vidhva', 'મહિલા', 'દીકરી', 'વિધવા', 'આંગણવાડી'],
            'education': ['student', 'scholarship', 'fee', 'hostel', 'digital', 'education', 'vidyarthi', 'shikshan', 'વિદ્યાર્થી', 'શિષ્યવૃત્તિ', 'શિક્ષણ'],
            'employment': ['job', 'skill', 'startup', 'msme', 'employment', 'rojgar', 'naukri', 'રોજગાર', 'નોકરી', 'કૌશલ્ય'],
            'health': ['health', 'hospital', 'medicine', 'treatment', 'arogya', 'dava', 'swasthya', 'આરોગ્ય', 'હોસ્પિટલ', 'દવા', 'સારવાર'],
            'housing': ['housing', 'home', 'rural', 'urban', 'awas', 'ghar', 'makan', 'આવાસ', 'ઘર', 'મકાન'],
            'senior': ['senior', 'pension', 'old', 'disability', 'vruddh', 'pension', 'વૃદ્ધ', 'પેન્શન', 'વિકલાંગ'],
            'food': ['food', 'ration', 'grain', 'ann', 'anaj', 'rashan', 'ખોરાક', 'રાશન', 'અનાજ'],
            'utility': ['electricity', 'water', 'transport', 'bus', 'gsrtc', 'vijli', 'pani', 'વીજળી', 'પાણી', 'બદ'],
            'business': ['business', 'loan', 'industry', 'dhandho', 'udhyog', 'vyapar', 'ધંધો', 'ઉદ્યોગ', 'વ્યાપાર'],
            'environment': ['solar', 'energy', 'environment', 'surya', 'paryavaran', 'સૌર', 'ઊર્જા', 'પર્યાવરણ'],
            'grievance': ['complaint', 'delay', 'help', 'fariyad', 'madad', 'ફરિયાદ', 'મદદ']
        }

        for topic, words in keywords.items():
            for word in words:
                if word in text:
                    return topic
        return None

    def get_scheme_info(self, topic):
        # Knowledge Base
        kb = {
            'agriculture': {
                'en': "🌾 **Agriculture & Farmers Schemes**\n\n1. **Khedut Khata**: Subsidies for seeds, fertilizers, and farm equipment.\n2. **Crop Insurance**: Pradhan Mantri Fasal Bima Yojana for crop loss.\n3. **Electricity**: Subsidized power for irrigation pumps.\n4. **Animal Husbandry**: Loans for cattle and dairy farming.",
                'gu': "🌾 **કૃષિ અને ખેડૂત કલ્યાણ યોજનાઓ**\n\n૧. **ખેડૂત ખાતા**: બિયારણ, ખાતર અને ખેતીના સાધનો માટે સબસિડી.\n૨. **પાક વીમો**: પાક નુકસાન માટે પ્રધાનમંત્રી ફસલ બીમા યોજના.\n૩. **વીજળી**: સિંચાઈ પંપ માટે સબસિડીવાળી વીજળી.\n૪. **પશુપાલન**: પશુ અને ડેરી ફાર્મિંગ માટે લોન."
            },
            'women': {
                'en': "👩 **Women & Child Welfare**\n\n1. **Vahali Dikri Yojana**: Financial assistance for girl child education and marriage.\n2. **Ganga Swarupa Yojana**: Monthly pension for widows.\n3. **Mahila Utkarsh Yojana**: Interest-free loans for women's self-help groups.",
                'gu': "👩 **મહિલા અને બાળ કલ્યાણ**\n\n૧. **વ્હાલી દીકરી યોજના**: દીકરીના શિક્ષણ અને લગ્ન માટે આર્થિક સહાય.\n૨. **ગંગા સ્વરૂપા યોજના**: વિધવા બહેનો માટે માસિક પેન્શન.\n૩. **મહિલા ઉત્કર્ષ યોજના**: મહિલા સ્વ-સહાય જૂથો માટે વ્યાજ મુક્ત લોન."
            },
            'education': {
                'en': "🎓 **Education & Students**\n\n1. **MYSY Scholarship**: Tuition fee assistance for meritorious students.\n2. **Digital Gujarat**: Scholarships for SC/ST/OBC students.\n3. **Namo Tablet**: Subsidized tablets for college students.",
                'gu': "🎓 **શિક્ષણ અને વિદ્યાર્થીઓ**\n\n૧. **MYSY શિષ્યવૃત્તિ**: તેજસ્વી વિદ્યાર્થીઓ માટે ટ્યુશન ફી સહાય.\n૨. **ડિજિટલ ગુજરાત**: SC/ST/OBC વિદ્યાર્થીઓ માટે શિષ્યવૃત્તિ.\n૩. **નમો ટેબ્લેટ**: કોલેજના વિદ્યાર્થીઓ માટે સબસિડીવાળા ટેબ્લેટ."
            },
            'employment': {
                'en': "💼 **Employment & Skill Development**\n\n1. **Anubandham Portal**: Job matching platform for employers and job seekers.\n2. **Apprenticeship Scheme**: Stipend support for on-the-job training.\n3. **Startup Gujarat**: Funding and mentorship for new startups.",
                'gu': "💼 **રોજગાર અને કૌશલ્ય વિકાસ**\n\n૧. **અનુબંધમ પોર્ટલ**: નોકરીદાતાઓ અને નોકરી શોધનારાઓ માટેનું પ્લેટફોર્મ.\n૨. **એપ્રેન્ટિસશીપ યોજના**: તાલીમ દરમિયાન સ્ટાઈપેન્ડ સહાય.\n૩. **સ્ટાર્ટઅપ ગુજરાત**: નવા સ્ટાર્ટઅપ માટે ફંડિંગ અને માર્ગદર્શન."
            },
            'health': {
                'en': "🏥 **Health & Medical**\n\n1. **PMJAY-MA Yojana**: Free medical treatment up to ₹10 Lakhs.\n2. **Chiranjeevi Yojana**: Free delivery services for pregnant women.\n3. **108 Ambulance**: Emergency medical services.",
                'gu': "🏥 **આરોગ્ય અને તબીબી સેવાઓ**\n\n૧. **PMJAY-MA યોજના**: ₹૧૦ લાખ સુધીની મફત સારવાર.\n૨. **ચિરંજીવી યોજના**: સગર્ભા સ્ત્રીઓ માટે મફત ડિલિવરી સેવા.\n૩. **૧૦૮ એમ્બ્યુલન્સ**: આપાતકાલીન તબીબી સેવાઓ."
            },
            'housing': {
                'en': "🏠 **Housing Schemes**\n\n1. **Pradhan Mantri Awas Yojana**: Subsidy for building/buying affordable houses.\n2. **Ambedkar Awas Yojana**: Housing assistance for SC/ST categories.",
                'gu': "🏠 **આવાસ યોજનાઓ**\n\n૧. **પ્રધાનમંત્રી આવાસ યોજના**: ઘર બનાવવા/ખરીદવા માટે સબસિડી.\n૨. **આંબેડકર આવાસ યોજના**: SC/ST વર્ગ માટે આવાસ સહાય."
            },
            'senior': {
                'en': "👴 **Senior Citizen & Social Security**\n\n1. **Niradhar Vruddh Pension**: Monthly pension for destitute senior citizens.\n2. **Divyang Pension**: Financial support for persons with disabilities.",
                'gu': "👴 **વરિષ્ઠ નાગરિક અને સામાજિક સુરક્ષા**\n\n૧. **નિરાધાર વૃદ્ધ પેન્શન**: નિરાધાર વરિષ્ઠ નાગરિકો માટે માસિક પેન્શન.\n૨. **દિવ્યાંગ પેન્શન**: વિકલાંગ વ્યક્તિઓ માટે આર્થિક સહાય."
            },
            'food': {
                'en': "🍚 **Food & Ration**\n\n1. **NFSA Ration Card**: Subsidized wheat, rice, and sugar.\n2. **Antyodaya Anna Yojana**: Food security for the poorest families.",
                'gu': "🍚 **અન્ન અને રાશન**\n\n૧. **NFSA રાશન કાર્ડ**: સબસિડીવાળા ઘઉં, ચોખા અને ખાંડ.\n૨. **અંત્યોદય અન્ન યોજના**: ગરીબ પરિવારો માટે અન્ન સુરક્ષા."
            },
            'utility': {
                'en': "⚡ **Electricity & Transport**\n\n1. **Surya Shakti Kisan Yojana**: Solar power for farmers.\n2. **GSRTC Concessions**: Discounted bus passes for students and seniors.",
                'gu': "⚡ **વીજળી અને પરિવહન**\n\n૧. **સૂર્ય શક્તિ કિસાન યોજના**: ખેડૂતો માટે સૌર ઊર્જા.\n૨. **GSRTC રાહત**: વિદ્યાર્થીઓ અને વરિષ્ઠ નાગરિકો માટે બસ પાસમાં છૂટ."
            },
            'business': {
                'en': "🏭 **Business & Industry**\n\n1. **Vajpayee Bankable Yojana**: Loans for small businesses and artisans.\n2. **Industrial Policy**: Incentives for setting up new industries.",
                'gu': "🏭 **ઉદ્યોગ અને વ્યવસાય**\n\n૧. **વાજપેયી બેંકેબલ યોજના**: નાના વ્યવસાયો અને કારીગરો માટે લોન.\n૨. **ઔદ્યોગિક નીતિ**: નવા ઉદ્યોગો સ્થાપવા માટે પ્રોત્સાહન."
            },
            'environment': {
                'en': "☀️ **Environment & Energy**\n\n1. **Solar Rooftop Scheme**: Subsidy for installing solar panels on homes.\n2. **E-Vehicle Subsidy**: Financial support for buying electric vehicles.",
                'gu': "☀️ **પર્યાવરણ અને ઊર્જા**\n\n૧. **સોલર રૂફટોપ યોજના**: ઘર પર સોલર પેનલ લગાવવા માટે સબસિડી.\n૨. **ઈ-વ્હીકલ સબસિડી**: ઇલેક્ટ્રિક વાહન ખરીદવા માટે આર્થિક સહાય."
            },
            'grievance': {
                'en': "📋 **Public Grievance Guidance**\n\nTo register a complaint regarding any government service:\n1. Visit **swagat.gujarat.gov.in**\n2. Call **CM Helpline: 1900**\n3. Contact your local Mamlatdar or TDO office.",
                'gu': "📋 **જાહેર ફરિયાદ માર્ગદર્શન**\n\nકોઈપણ સરકારી સેવા અંગે ફરિયાદ કરવા માટે:\n૧. **swagat.gujarat.gov.in** ની મુલાકાત લો.\n૨. **CM હેલ્પલાઇન: ૧૯૦૦** પર કોલ કરો.\n૩. તમારી સ્થાનિક મામલતદાર અથવા TDO કચેરીનો સંપર્ક કરો."
            }
        }
        
        return kb.get(topic, {}).get(self.language, self.get_out_of_scope_response())

    def get_out_of_scope_response(self):
        if self.language == 'en':
            return "I'm sorry, this question is not related to Gujarat Government schemes or services.\nThis is not within my field."
        else:
            return "માફ કરશો, તમારો પ્રશ્ન ગુજરાત સરકારની યોજનાઓ અથવા સેવાઓ સાથે સંબંધિત નથી.\nઆ મારા કાર્યક્ષેત્રમાં આવતું નથી."
