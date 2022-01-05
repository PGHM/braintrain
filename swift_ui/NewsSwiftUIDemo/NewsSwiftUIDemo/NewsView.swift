//
//  Copyright © 2022 Jussi Päivinen. All rights reserved.
//

import SwiftUI

struct NewsView: View {
    let teasers: [Teaser]

    var body: some View {
        List(teasers) { teaser in
            TeaserView(teaser: teaser)
        }
        .listStyle(.plain)
    }
}

struct NewsView_Previews: PreviewProvider {
    static var previews: some View {
        NewsView(teasers: TeaserProvider.frontPageTeasers)
            .previewLayout(.sizeThatFits)
    }
}
