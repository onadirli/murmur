import enum

class State(enum.Enum):
    AL = "AL"
    AK = "AK"
    AZ = "AZ"
    AR = "AR"
    CA = "CA"
    CO = "CO"
    CT = "CT"
    DE = "DE"
    FL = "FL"
    GA = "GA"
    HI = "HI"
    ID = "ID"
    IL = "IL"
    IN = "IN"
    IA = "IA"
    KS = "KS"
    KY = "KY"
    LA = "LA"
    ME = "ME"
    MD = "MD"
    MA = "MA"
    MI = "MI"
    MN = "MN"
    MS = "MS"
    MO = "MO"
    MT = "MT"
    NE = "NE"
    NV = "NV"
    NH = "NH"
    NJ = "NJ"
    NM = "NM"
    NY = "NY"
    NC = "NC"
    ND = "ND"
    OH = "OH"
    OK = "OK"
    OR = "OR"
    PA = "PA"
    RI = "RI"
    SC = "SC"
    SD = "SD"
    TN = "TN"
    TX = "TX"
    UT = "UT"
    VA = "VA"
    WA = "WA"
    WV = "WV"
    WI = "WI"
    WY = "WY"


# TODO: change the enum values to be more standardized (ex. "Bachelor’s Degree" -> "BACHELORS")
# TODO: add separate localization support for human-readable enum values

class EducationLevel(enum.Enum):
    BACHELORS = "Bachelor’s Degree"
    HIGH_SCHOOL = "High School"
    DOCTORATE = "Doctorate"
    MASTER = "Master’s Degree"
    SOME_COLLEGE = "Some College"
    ASSOCIATE = "Associate Degree"

class Gender(enum.Enum):
    MALE = "Male"
    FEMALE = "Female"
    NON_BINARY = "Non-binary"
    CHOOSE_NOT_TO_DISCLOSE = "Prefer not to disclose"

class IncomeLevel(enum.Enum):
    LOW = "Low"
    LOWER_MIDDLE = "Lower-Middle"
    MIDDLE = "Middle"
    UPPER_MIDDLE = "Upper-Middle"
    HIGH = "High"

class SentimentType(enum.Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"


def format_state(state: str) -> State:
    #TODO: expand to be take in state name or abbreviation
    #TODO: add error handling
    return State(state.upper())

def format_zipcode(zipcode: str) -> str:
    #TODO: add real error handling
    if not zipcode or zipcode.strip() == "":
        return None
    if len(zipcode) > 5:
        return zipcode[:5]
    else:
        return zipcode.zfill(5)

def format_education_level(education_level: str) -> EducationLevel:
    #TODO: add error handling and better mapping
    return EducationLevel(education_level)

def format_gender(gender: str) -> Gender:
    #TODO: add error handling and better mapping
    return Gender(gender)

def format_income_level(income_level: str) -> IncomeLevel:
    #TODO: add error handling and better mapping
    return IncomeLevel(income_level)
