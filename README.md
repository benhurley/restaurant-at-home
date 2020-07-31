# Are you missing indoor dining as much as I am?
In the wake of Covid-19, delivery and takeout food orders have replaced indoor dining in many parts of the US. A major component as to why a customer chooses a particular restaurant is the <i>experience</i>, where the actual meal may only play a minor role. Popular delivery and takeout apps are missing a crucial component to the dining experience, which is the atmosphere while you are eating.

This project is a POC to help recreate (as much as possible) the vibe at some of your favorite restaurants while we wait for indoor dining to return. With data such as how to set your table, lighting, music, etc. you can get closer than ever before. If nothing else, it serves as an idea for date-night or a family meal.

There are two ways we can begin aggregating restaurant data:

1. Web-scraping positive online reviews
2. Allowing the restaurant to submit a form so customers can recreate the experience at home

To start, a wireframe with dummy-data has been created as we work through how the UI should look.

## Contact

If you would like to contribute to the project, please reach out to me at benfromtech@gmail.com

## Requirements

1. Node.js (10.13.0^)
2. Yarn
3. Python3

## Quick Start

Install dependencies

```bash
yarn install
```

Setup the back end

```bash
cd api/
```

```bash
python3 -m venv venv
```

```bash
. venv/bin/activate
```

```bash
pip install flask
```

```bash
pip install python-dotenv
```


```bash
cd ..
```

Start the backend

```bash
yarn start-api
```

Start the frontend

```bash
yarn start
```

-----------------------

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

### Analyzing the Bundle Size

This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

### Making a Progressive Web App

This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

### Advanced Configuration

This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

### Deployment

This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

### `yarn build` fails to minify

This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify
