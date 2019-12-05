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
    // fetch(`/api/articles/`)
    //   .then(results => {
    //     return results.json();
    //   })
    //   .then(data => {
    //     let articles = data.map(item => {
    //       return (
    //         <div key={`article` + item.id}>
    //           <a href=''>{item.title}</a>
    //         </div>
    //       );
    //     });
    //     this.setState({ articles: articles });
    //     console.log('Articles: ', this.state.articles);
    //   });

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
        console.log('Topics: ', this.state.topics);
      });

    fetch(`/api/topics/1/`)
      .then(results => {
        return results.json();
      })
      .then(data => {
        // console.log(data);
        let topic = data.topic;

        this.setState({ one_topic: topic });
        console.log('One topic: ', this.state.one_topic);
      });

    fetch(`/api/comments/`)
      .then(results => {
        return results.json();
      })
      .then(data => {
        let comments = data.map(item => {
          return (
            <div key={`comment` + item.id}>
              <a href='#'>
                {item.message} - {item.author} - {item.created_on} -{' '}
                {item.article}
              </a>
            </div>
          );
        });
        this.setState({ comments: comments });
        console.log('Comments: ', this.state.comments);
      });

    fetch(`/api/comments/2/`)
      .then(results => {
        return results.json();
      })
      .then(data => {
        console.log(data.article);
        let comment = (
          <div key={`comment` + data.id}>
            <a href='#'>
              {data.message} - {data.author} - {data.created_on} -{' '}
              {data.article}
            </a>
          </div>
        );

        this.setState({ one_comment: comment });
        console.log('One comment: ', this.state.one_comment);
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
          <br />
          <br />

          <p>List of all topics:</p>
          {this.state.topics}
          <br />
          <br />
          <br />

          <p>Just 1 topic:</p>
          {this.state.one_topic}
          <br />
          <br />
          <br />

          <p>List of all comments:</p>
          {this.state.comments}
          <br />
          <br />
          <br />

          <p>Just 1 comment:</p>
          {this.state.one_comment}
          <br />
          <br />
          <br />
        </section>
      </main>
    );
  }
}
