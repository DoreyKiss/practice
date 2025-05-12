# Setting up node

```bash
    node --version
    nvm install 18
    nvm use 18
    npm init # will initialize the package for you
    npm install -g typescript
    tsc --version
    tsc --init
    tsc --init --sourceMap --rootDir src --outDir dist
    tsc # for compiling

    # i want a ts watch so it is compiling for me
    npm i --save-dev typescript

    task configure default build task: select tsc: watch

    task run build task
```

