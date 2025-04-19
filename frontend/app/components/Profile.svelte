<script lang="ts">
  import { type RespondentRead } from '../../lib/types';
  
  export let respondent: RespondentRead;
</script>

<div class="profile-card">
  <div class="profile-header">
    <h3>Respondent Profile</h3>
    <span class="id">Imported ID: {respondent.upload_id}</span>
  </div>
  
  <div class="profile-content">
    <div class="demographics">
      <div class="info-row">
        <span class="label">Age:</span>
        <span class="value">{respondent.age || 'N/A'}</span>
      </div>
      <div class="info-row">
        <span class="label">Gender:</span>
        <span class="value">{respondent.gender}</span>
      </div>
      <div class="info-row">
        <span class="label">Location:</span>
        <span class="value">{respondent.city}, {respondent.state || 'N/A'}</span>
      </div>
    </div>
    
    <div class="socioeconomic">
      <div class="info-row">
        <span class="label">Income:</span>
        <span class="value">{respondent.income_level || 'N/A'}</span>
      </div>
      <div class="info-row">
        <span class="label">Education:</span>
        <span class="value">{respondent.education_level || 'N/A'}</span>
      </div>
    </div>
  </div>
</div>

<style>
  .profile-card {
    width: 400px;
    height: 200px;
    background: #1e1e1e;
    border-radius: 8px 0px 0px 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .profile-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #333;
    padding-bottom: 8px;
  }

  h3 {
    margin: 0;
    font-size: 1.1rem;
    color: #ffffff;
  }

  .id {
    font-size: 0.8rem;
    color: rgba(160, 160, 160, 0.7);
  }

  .profile-content {
    display: flex;
    gap: 24px;
    flex: 1;
  }

  .demographics, .socioeconomic {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .info-row {
    display: flex;
    justify-content: space-between;
    font-size: 0.9rem;
  }

  .label {
    color: rgba(160, 160, 160, 0.7);
  }

  .value {
    color: #ffffff;
    font-weight: 500;
  }

  :global(.dark) .profile-card {
    --bg-color: #1a1a1a;
    --border-color: #333;
    --text-primary: #f5f5f5;
    --text-secondary: #a0a0a0;
  }
</style>
