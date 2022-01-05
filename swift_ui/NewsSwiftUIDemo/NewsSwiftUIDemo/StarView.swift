//
//  Copyright © 2022 Jussi Päivinen. All rights reserved.
//

import SwiftUI

struct StarView: View {
    var body: some View {
        Image("star")
            .resizable()
            .scaledToFit()
            .foregroundColor(Color.yellow)
            .background(
                Image("space").resizable()
            )
            .clipShape(Circle())
            .overlay(
                Circle().strokeBorder(.red, lineWidth: 3)
            )
            .shadow(radius: 5)
    }
}

struct StarView_Previews: PreviewProvider {
    static var previews: some View {
        StarView()
    }
}
