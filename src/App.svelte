<script>
	import qs from './q.json';

	// shuffle question

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

	// random get one question

	let q = qs[Math.floor(Math.random()*qs.length)];

	// play question

	function play() {
		window.speechSynthesis.speak(new SpeechSynthesisUtterance(q.question));
	}

	// hidden question

	let show = false;

	document.body.onkeyup = function(e){
		if(e.code == 'Space'){
			play();
			setTimeout(function(){ show = true; }, 5000);	
		}
	}

	// record audio

	let chunks = [];
	let mediaRecorder;

	if (navigator.mediaDevices.getUserMedia) {
		console.log('getUserMedia supported.');
		const constraints = { audio: true };

		let onSuccess = function(stream) {
			mediaRecorder = new MediaRecorder(stream);
			mediaRecorder.onstop = function(e) {
				let audio = document.getElementById("audio");
				audio.controls = true;
				const blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });
				const audioURL = window.URL.createObjectURL(blob);
				audio.src = audioURL;
				console.log("recorder stopped");
			}
			mediaRecorder.ondataavailable = function(e) {
				chunks.push(e.data);
			}
		}

		let onError = function(err) {
			console.log('The following error occured: ' + err);
		}

		navigator.mediaDevices.getUserMedia(constraints).then(onSuccess, onError);
	}

	let recordState = 0; // -1 - disable, 0 - init, 1 - record, 2 - stop, 3 - play

	function record() {
		if (!navigator.mediaDevices.getUserMedia) {
			console.log('getUserMedia not supported on your browser!');
			return;
		}

		if (recordState === 0) {
			// start record
			recordState = 1;
			mediaRecorder.start();
			console.log(mediaRecorder.state);
			console.log("recorder started");
		} else if (recordState === 1) {
			// stop record
			recordState = 2;
			mediaRecorder.stop();
			console.log(mediaRecorder.state);
			console.log("recorder stopped");
		}
	}

</script>

<main class="bg-gray-200 p-8 m-8 rounded-lg">
	{#if !show}
	<p style='color: gray'>&lt;press spacebar to play question&gt;</p>
	{/if}
	{#if show}
    	<p>{q.question}</p>
	{/if}
</main>

<div class="flex items-center justify-center">
	{#if recordState === 0 || recordState === 1}
		<div class="bg-green-600 py-3 px-6 rounded-full flex items-center justify-center text-white" on:click="{record}">
			{#if recordState === 0}
				record your answer
			{/if}
			{#if recordState === 1}
				stop record
			{/if}
		</div>
	{/if}
	{#if recordState === 2}
		<audio id="audio"></audio>
	{/if}
</div>

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