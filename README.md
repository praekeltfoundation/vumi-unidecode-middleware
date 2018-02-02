# vumi-unidecode-middleware
[Vumi][vumi] middleware that runs message content through unidecode

## Using the middleware

The path to the middleware class is
`vumi_unidecode_middleware.UnidecodeMiddleware`.

For more information on how to run vumi middleware, please consult the [vumi
middleware documentation][vumi_middleware].

## Testing

To run the tests, install the dependancies and use the trial test runner:

    pip install -e .
    trial vumi_unidecode_middleware


[vumi]: https://github.com/praekelt/vumi
[vumi_middleware]: https://vumi.readthedocs.io/en/latest/middleware/index.html
