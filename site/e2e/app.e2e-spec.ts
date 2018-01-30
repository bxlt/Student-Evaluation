import { BioPage } from './app.po';

describe('bio App', () => {
  let page: BioPage;

  beforeEach(() => {
    page = new BioPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
