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
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
      })
      .then(data => {
        let articles = data.map(item => {
          return (
            <div key={`article` + item.id}>
              <a href=''>
                {item.title} - {item.slug} - item.author - {item.updated_on} -
                {item.content} - {item.created_on} - Topics:{item.topics} -
                {item.status}
              </a>
            </div>
          );
        });
        this.setState({ articles: articles });
        console.log('Articles: ', this.state.articles);
      })
      .catch(error => {
        this.setState({ articles: 'There are no articles.' });
        console.log(
          'There has been a problem with your fetch operation: ',
          error.message
        );
      });

    fetch(`/api/articles/18/`)
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
      })
      .then(data => {
        let article = (
          <div key={`comment` + data.id}>
            <a href='#'>
              {data.title} - {data.slug} - data.author - {data.updated_on} -
              {data.content} - {data.created_on} - Topics:{data.topics} -
              {data.status}
            </a>
          </div>
        );
        this.setState({ one_article: article });
        console.log('One article: ', this.state.one_article);
      })
      .catch(error => {
        this.setState({ one_article: 'There is no article.' });
        console.log(
          'There has been a problem with your fetch operation: ',
          error.message
        );
      });

    fetch(`/api/topics/`)
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
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
      })
      .catch(error => {
        this.setState({ topics: 'There are no topics.' });
        console.log(
          'There has been a problem with your fetch operation: ',
          error.message
        );
      });

    fetch(`/api/topics/18/`)
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
      })
      .then(data => {
        // console.log(data);
        let topic = data.topic;

        this.setState({ one_topic: topic });
        console.log('One topic: ', this.state.one_topic);
      })
      .catch(error => {
        this.setState({ one_topic: 'There is no topic.' });
        console.log(
          'There has been a problem with your fetch operation: ',
          error.message
        );
      });

    fetch(`/api/comments/`)
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
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
      })
      .catch(error => {
        this.setState({ comments: 'There are no comments.' });
        console.log(
          'There has been a problem with your fetch operation: ',
          error.message
        );
      });

    fetch(`/api/comments/28/`)
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
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
      })
      .catch(error => {
        this.setState({ one_comment: 'There is no comment.' });
        console.log(
          'There has been a problem with your fetch operation: ',
          error.message
        );
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

          <p>Just 1 article:</p>
          {this.state.one_article}
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
