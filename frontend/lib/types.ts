export type Gender = 'Male' | 'Female' | 'Non-binary' | 'Prefer not to disclose';
export type State = 'AL' | 'AK' | 'AZ' | 'AR' | 'CA' | 'CO' | 'CT' | 'DE' | 'FL' | 'GA' | 'HI' | 'ID' | 'IL' | 'IN' | 'IA' | 'KS' | 'KY' | 'LA' | 'ME' | 'MD' | 'MA' | 'MI' | 'MN' | 'MS' | 'MO' | 'MT' | 'NE' | 'NV' | 'NH' | 'NJ' | 'NM' | 'NY' | 'NC' | 'ND' | 'OH' | 'OK' | 'OR' | 'PA' | 'RI' | 'SC' | 'SD' | 'TN' | 'TX' | 'UT' | 'VT' | 'VA' | 'WA' | 'WV' | 'WI' | 'WY';
export type IncomeLevel = 'Low' | 'Lower-Middle' | 'Middle' | 'Upper-Middle' | 'High';
export type EducationLevel = 'High School' | 'Some College' | 'Bachelor\'s Degree' | 'Master\'s Degree' | 'Doctorate';
export type SentimentType = 'Positive' | 'Negative' | 'Neutral';

export interface Core {
  id: string;
  created_at: string;
}

export interface RespondentRead extends Core {
  upload_id?: number;
  age?: number;
  gender: Gender;
  zip_code?: string;
  city?: string;
  state?: State;
  income_level?: IncomeLevel;
  education_level?: EducationLevel;
}

export interface QuestionRead extends Core {
  question_name: string;
  question_text: string;
}

export interface QuestionResponseRead extends Core {
  question: QuestionRead;
  respondent_id: string;
  response_value: string;
}

export interface SurveyResponseRead extends Core {
  respondent: RespondentRead;
  sentiment: SentimentType;
  question_responses: QuestionResponseRead[];
} 