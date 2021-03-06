# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.firefox.home import FirefoxHomePage


@pytest.mark.skipif(reason='https://github.com/mozilla/bedrock/issues/6456')
@pytest.mark.sanity
@pytest.mark.nondestructive
def test_download_buttons_displayed(base_url, selenium):
    page = FirefoxHomePage(selenium, base_url).open()
    assert page.primary_download_button.is_displayed
    assert page.secondary_download_button.is_displayed
