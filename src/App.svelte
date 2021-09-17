<script>
	import qs from './q.json';
	let q = qs[Math.floor(Math.random()*qs.length)];
</script>

<main class="bg-gray-200 p-8 m-8 rounded-lg">
	<p>{q.question}</p>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	p {
		color: purple;
		font-family: 'Comic Sans MS', cursive;
		font-size: 2em;
	}
</style>