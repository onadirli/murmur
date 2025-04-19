<script lang="ts">
  import { onMount } from 'svelte';
  import ResultRow from '../components/ResultRow.svelte';
  import { type SurveyResponseRead } from '../../lib/types';

  let responses: SurveyResponseRead[] = [];
  let error: string | null = null;

  onMount(async () => {
    try {
      const res = await fetch('http://localhost:8001/surveys/');
      if (!res.ok) throw new Error('Failed to fetch survey responses');
      responses = await res.json();
    } catch (e) {
      error = e instanceof Error ? e.message : 'An unknown error occurred';
    }
  });
</script>

<main>
  <h1>Whispr</h1>

  {#if error}
    <div class="error">{error}</div>
  {:else if responses.length === 0}
    <div class="empty-state">No survey responses found</div>
  {:else}
    <div class="responses-container">
      {#each responses as response}
        <ResultRow {response} />
      {/each}
    </div>
  {/if}

  <div class="footer">
    <p>Created by Orkhan Nadirli for Murmuration Interview, Copyright 2025</p>
  </div>
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
  }

  main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
  }

  h1 {
    color: #333;
    margin-bottom: 2rem;
  }

  .responses-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .error {
    color: #dc3545;
    padding: 1rem;
    background: #fff;
    border-radius: 8px;
    margin-bottom: 1rem;
  }

  .empty-state {
    color: #666;
    text-align: center;
    padding: 2rem;
    background: #fff;
    border-radius: 8px;
  }

  .footer {
    position: fixed;
    bottom: 0;
    right: 5vw;
  }
</style>
