MILADY_TOKEN = 0x227c7DF69D3ed1ae7574A1a7685fDEd90292EB48

def test_minter(project, accounts):
    d = accounts[-1]
    print(d.balance)
    minter = project.MiladyMinter.deploy("miladyminter", "MLM", "test.com", "MLM", "1MAINNET", 100, sender=d)
    print(minter)
    tx = minter.safe_mint(sender=d, value=100)
    print(tx.events)
    assert minter.balanceOf(d) == 1
    print(project.ERC20.at(MILADY_TOKEN).balanceOf(minter))
