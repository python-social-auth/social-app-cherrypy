# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

### Changed

- Modified model and access code to work with SQLAlchemy version 2 (Issue #2)
- Updated packaging information files per PEP 517, PEP 518 (Issue #3)
- Restricted Python minimum working version to 3.7 or higher to align with SQLAlchemy 2 (Issue #2)
- Fixed csrfmiddlewaretoken argument error when calling disconnect method in view.py when disconnecting social connections (Issue #4)

## [1.0.0](https://github.com/python-social-auth/social-app-cherrypy/releases/tag/1.0.0) - 2017-01-22

### Added

- Added `load_strategy` utility
- Added partial pipeline db storage solution

## [0.0.1](https://github.com/python-social-auth/social-app-cherrypy/releases/tag/0.0.1) - 2016-11-27

### Changed

- Split from the monolitic [python-social-auth](https://github.com/omab/python-social-auth)
  codebase
