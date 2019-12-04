// Vanilla React:
import React, { Component } from 'react';

// Third-party libraries:

// Smaller components:

import './Main.css';

export default class Main extends Component {
  constructor() {
    super();
    this.state = {
      articles: []
    };
  }

  // handleListArticles = () => {
  //   // get (`https://thiswillfail.me/api/?results=5`) {
  //   //   let promise = new Promise((resolve, reject) => {
  //   //      fetch(url)
  //   //         .then(response => {
  //   //            resolve(response.json().then(data => (
  //   //               data.results
  //   //            )))
  //   //         })
  //   //        .catch(response => {
  //   //           reject("Api call failed!")
  //   //        })
  //   //      })
  //   //     .then(response => {
  //   //        console.log(response)
  //   //     })
  //   //     .catch(response => {
  //   //        console.log('error: ' + response)
  //   //     })
  //   };
  // };

  componentDidMount() {
    // this.handleListArticles();

    // fetch(`https://randomuser.me/api/?results=20`)
    fetch(`/api/articles/`)
      .then(results => {
        return results.json();
      })
      .then(data => {
        let articles = data.map(item => {
          return (
            <div key={`article` + item.id}>
              <a href=''>{item.title}</a>
            </div>
          );
        });
        this.setState({ articles: articles });
        console.log('state', this.state.articles);
      });

    fetch(`/api/topics/`)
      .then(results => {
        return results.json();
      })
      .then(data => {
        let topics = data.map(item => {
          return (
            <div key={`topic` + item.id}>
              <a href=''>{item.topic}</a>
            </div>
          );
        });
        this.setState({ topics: topics });
        console.log('state', this.state.topics);
      });
  }

  render() {
    return (
      <main className='jumbotron jumbotron-fluid'>
        <br />
        <br />
        <br />
        <section className='section1'>
          <p>List of all articles:</p>
          {this.state.articles}
          <br />

          <p>List of all topics:</p>
          {this.state.topics}
        </section>
      </main>
    );
  }
}
