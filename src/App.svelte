<script>
	import qs from './q.json';

	function shuffle(array) {
		let currentIndex = array.length,  randomIndex;

		// While there remain elements to shuffle...
		while (currentIndex != 0) {

			// Pick a remaining element...
			randomIndex = Math.floor(Math.random() * currentIndex);
			currentIndex--;

			// And swap it with the current element.
			[array[currentIndex], array[randomIndex]] = [
			array[randomIndex], array[currentIndex]];
		}

		return array;
	}

	shuffle(qs);

	let q = qs[Math.floor(Math.random()*qs.length)];

</script>

<main class="bg-gray-200 p-8 m-8 rounded-lg">
	<p>{q.question}</p>
</main>

<style>
	p {
		color: purple;
		font-family: 'Comic Sans MS', cursive;
		font-size: 2em;
	}
	
	main {
		text-align: center;
		padding: 1em;
		margin: 10 auto;
	}
</style>