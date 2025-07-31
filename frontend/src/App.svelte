<script>
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
</script>

<main>

  <div>
    <h1>Register</h1>
    

    <div>
    <form>
      <label for="username">Name: </label>
      <input id="name" type="text"/>

      <label for="username">Username: </label>
      <input id="username" type="text"/>

      <label for="email">Email: </label>
      <input id="email" type="text"/>

      <label for="password">Password: </label>
      <input id="password" type="text"/>

      <label for="confirm password">Confirm Password: </label>
      <input id="confirm-password" type="text"/>
    </form>
  </div>
    <button type="button">Submit</button>
  </div>
</main> 

<style>
  form {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
		max-width: 300px;
		margin: 1rem auto ;
	}
  
</style>
