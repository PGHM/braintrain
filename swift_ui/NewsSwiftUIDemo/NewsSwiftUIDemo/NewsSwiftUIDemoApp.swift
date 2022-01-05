//
//  Copyright © 2021 Jussi Päivinen. All rights reserved.
//

import SwiftUI

@main
struct NewsSwiftUIDemoApp: App {
    var body: some Scene {
        WindowGroup {
            NewsView(teasers: TeaserProvider.frontPageTeasers)
        }
    }
}
