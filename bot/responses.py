import random

response = {
    "areRollupsSafe": "\n\n Absolutely! Optimistic Rollups are safe as long as Ethereum itself is \"live\" (i.e. not actively censoring transactions). This security model is backed by a system of \"fraud proofs,\" whereby users are paid to reveal bad transaction results published to the OE chain.",
    "delay": "\n\n Withdrawal delays exist to keep your funds safe. Optimistic Rollups have to make use of a \"fraud proof window\" (sometimes called a \"challenge period\"). This window is a period of time after a transaction result has been published during which users can, if necessary, demonstrate that the published result was incorrect. This period must be long enough that an invalid result can be detected and reverted, even under extreme conditions. \n \n Currently, community consensus is that this period should be on the order of approximately one week to maximize safety of user assets. Since a result can potentially be reverted during the fraud proof window, applications on Ethereum will typically choose to wait until the window has expired to make decisions about results from the Optimistic Ethereum chain. \n \n As a result, we see a delay of about a week when moving assets back onto Ethereum.",
    "ethNatively": "\n\n Optimistic Ethereum doesn't use ETH natively in the same way that Ethereum does. Instead, ETH is represented as an ERC20 token that can be transferred and manipulated, essentially like the native version of [wrapped ETH (wETH)](https://weth.io/). You're still fully capable of transferring ETH between accounts with the added benefit of being able to avoid a separate token like wETH. The Layer 2 ETH ERC20 contract currently resides at this special Layer 2 address `0x4200000000000000000000000000000000000006.` \n \n :warning: Note!: The [eth_getBalance JSON-RPC call](https://eth.wiki/json-rpc/API#eth_getBalance) will retrieve a balance by querying the ETH ERC20 contract and therefore will remain useful for wallets.",
    "ethVsOptimism": "\n\n Optimistic Ethereum (OE) is mostly identical to Ethereum. You can create and interact with Solidity smart contracts (like you would on Ethereum) using the same wallet software you're already familiar with! Simply connect your wallet to an OE node and you're ready to go! :raised_hands: \n \n However, there're a few very minor differences between OE and Ethereum that developers may have to account for. For instance, we disable infrequently used operations like `CALLCODE`. If you're a developer, these differences could potentially require minor tweaks to your contract code. Please refer to the [Complete EVM/OVM Comparison ](https://community.optimism.io/compare) for a full list of differences.",
    "gasFees": "\n\n Fees are paid in WETH based on your gasPrice * gasLimit. Here's how we're implementing the fee estimation at the moment: \n * Modify eth_estimateGas(tx) to return dataPricetx.size + executionPricetx.gasUsed. \n * Add rollup_dataPrice which returns the current dataPrice, and rollup_executionPrice that returns the current congestion gas price on L2. \n * Modify gasPrice to return 0.1 gwei or 1 gwei. \n * Periodically set dataPrice=L1.eth_gasPrice and then set executionPrice= https://hackmd.io/SE741g9YT62P-PPdHnGH7w?view \n * Make sure that gasUsed is calculated correctly & that we always pass in max gasLimit in `state_transition.go`",
    "isSideChain": "\n\n Nope! Sidechains are their own blockchain systems with entirely separate consensus mechanisms. Optimistic Ethereum (OE) lives inside of Ethereum as a series of smart contracts capable of executing Ethereum transactions. Whereas sidechains rely on their own consensus mechanisms for security, OE relies on the security of Ethereum itself.",
    # "mainnetTimeline": "\n\n Our public mainnet is launching in March! :hooray:",
    "optimismExplainer": "\n\n Optimistic Ethereum (OE) is simply an app inside Ethereum that executes transactions more efficiently than Ethereum itself. It's based on the concept of the [Optimistic Rollup](https://medium.com/plasma-group/ethereum-smart-contracts-in-l2-optimistic-rollup-2c1cef2ec537), a construction that allows us to \"optimistically\" publish transaction results without actually executing those transactions on Ethereum (most of the time). OE makes transactions cheaper, faster, and smarter.",
    # Commenting this out because it interferes with "ethVsOptimism"
    # "optimismVsZK": "\n\n wants to know the difference between ZK Rollups and Optimistic Rollups",
    "willHaveToken": "\n\n OptimismPBC has no plans for any token. Sorry! 🙁",
    "hasToken": "\n\n OptimismPBC has no plans for any token. Sorry! 🙁",
}

greetings = [
    "Hey there!",
    "Hello!",
    "Great question!"
    "Hey!",
    "Neat question!",
    "Thanks for asking!",
    "Hello there!",
    "I've been waiting for this question!",
    "Salutations!",
    "Good evening, fren."
]

appreciation = [
    "My pleasure! Feel free to ask any other questions!",
    "At your service!",
    "Any day, my fren!",
    "It's what I was made to do <3 ",
    "Just doing my job 😃"
]