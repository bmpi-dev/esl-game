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

	// play question
	window.onload = function() {
		window.speechSynthesis.speak(new SpeechSynthesisUtterance(q.question));
	}

	let show = false;

	document.body.onkeyup = function(e){
		if(e.code == 'Space'){
			show = true;
		}
	}

</script>

<main class="bg-gray-200 p-8 m-8 rounded-lg" onclick="showQuestion">
	{#if !show}
	<p style='color: gray'>&lt;press spacebar to show question&gt;</p>
	{/if}
	{#if show}
    	<p>{q.question}</p>
	{/if}
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