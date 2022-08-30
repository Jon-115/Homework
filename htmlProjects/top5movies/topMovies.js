
let movieTitle = document.getElementById('movie')
let movitePoster = document.getElementById('poster')
const getMovies = () => {
    fetch('https://api.themoviedb.org/3/movie/popular?api_key=c550a946dcbfd4b30a86667a80d06ad8&language=en-US&page=1&region=US')
        .then(response => {
            return response.json();
        })
        .then(data => {
            for (let i = 0; i <= 4; i++) {
                mTitle = data.results[i].title
                mPoster = data.results[i].poster_path
                mOver = data.results[i].overview
                let movieTitle = document.getElementById('movie' + i)
                let temp = 'https://image.tmdb.org/t/p/w500' + mPoster
                document.getElementById('poster' + i).src = temp
                let movieOver = document.getElementById('o' + i)
                console.log(mTitle)
                console.log(mPoster)
                movieTitle.innerText = mTitle
                movieOver.innerText = mOver
            }
            console.log(data)
        })
}