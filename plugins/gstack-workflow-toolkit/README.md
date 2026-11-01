# gstack Workflow Toolkit

A skills-first plugin inspired by public project [garrytan/gstack](https://github.com/garrytan/gstack). It packages portable workflow guidance rather than copying gstack's executable code, browser binaries, or Claude-specific slash-command setup.

## Included workflows

- Product discovery and scope challenge
- Architecture and code review
- Root-cause debugging
- QA and security review planning
- Release verification and honest reporting

## Attribution and scope

Inspired by gstack's published README, skills overview, Builder Ethos, and agent digest. The source repository declares the MIT license; see [LICENSE](LICENSE). This package is an independently written workflow adaptation and is not affiliated with or endorsed by Garry Tan or Y Combinator. It does not implement or imply a live browser, static analyzer, vulnerability scanner, git client, CI runner, or deployment connector.

## Use

Invoke the relevant skill in a supported host and provide the repository diff, product brief, plan, test output, logs, or target URL that the workflow needs. Instructions distinguish proposed checks from checks that were actually run.
