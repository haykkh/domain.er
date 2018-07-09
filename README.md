# domain.er
> Tool to find domains that utilize the tld in the domain


![](header.png)


## Usage example
```sh
$ python domainer.py [--tld TLD] [--words WORDS] [--domains DOMAINS]
```
Saves a list of ``WORDS`` that use a ``TLD`` as the ending of the ``DOMAINS`` to a file.

e.g

```sh
$ python domainer.py -t tlds.txt -w words.txt -d domains.txt
$ Done! Check domains.txt
```

```sh
--tld, -t TLD
                    list of top level domains (tlds), default iana.org list if left empty
  
--words, -w WORDS
                    list of words to search, defaults to 1000.txt (a list of the 1000 most popular used words)

--domains, -d DOMAINS
                    file to output to, defaults to domains.txt
```


## Meta

Hayk Khachatryan –  hi@hayk.io

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/haykkh/](https://github.com/haykkh/)

## Contributing

1. Fork it (<https://github.com/haykkh/domain.er/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki