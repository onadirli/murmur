<script lang="ts">
  import { type SurveyResponseRead } from '../../lib/types';
  import Profile from './Profile.svelte';
  
  export let response: SurveyResponseRead;
</script>

<div class="result-row">
  <div class="profile-section">
    <Profile respondent={response.respondent} />
  </div>
  
  <div class="responses-section">
    <div class="column">
      {#each response.question_responses.slice(0, 3) as qr}
        <div class="response-item">
          <div class="question-text">{qr.question.question_text}</div>
          <div class="response-value">{qr.response_value}</div>
        </div>
      {/each}
    </div>
    <div class="column">
      {#each response.question_responses.slice(3) as qr}
        <div class="response-item">
          <div class="question-text">{qr.question.question_text}</div>
          <div class="response-value">{qr.response_value}</div>
        </div>
      {/each}
    </div>
  </div>
</div>

<style>
  .result-row {
    display: flex;
    background: #2a2a2a;
    border-radius: 16px;
    margin-bottom: 5px;
  }

  .profile-section {
    flex-shrink: 0;
  }

  .responses-section {
    flex: 1;
    display: flex;
    padding: 16px;
  }

  .column {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .response-item {
    display: flex;
    flex-direction: column;
    gap: 4px;
    text-align: left;
  }

  .question-text {
    font-size: 0.8rem;
    color: #888;
    text-align: left;
  }

  .response-value {
    font-size: 1.1rem;
    color: #e0e0e0;
    font-weight: 500;
    text-align: left;
  }
</style>
