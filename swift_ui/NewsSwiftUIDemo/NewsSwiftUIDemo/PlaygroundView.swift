//
//  Copyright © 2021 Jussi Päivinen. All rights reserved.
//

import SwiftUI

struct PlaygroundView: View {
    var body: some View {
        VStack(spacing: 20.0) {
            Text("Foobar")
                .padding()
                .font(.title)
                .foregroundColor(.red)
            StarView()
                .frame(width: 200)
                .padding()
                .offset(x: -10, y: 10)
            Text("Lisää")
                .font(.custom("Helvetica", size: 30))
            Text("Näitähän saa monta")
            Group() {
                HStack(alignment: .center, spacing: 20) {
                    Text("Aika on:")
                    Text(DateInterval(start: Date(), duration: 10))
                    Text("Mitäs sitten kun on paljon asioita niin mitä sitten käy")
                    Text("Vielä pari lisäää")
                    Text("MOOOOORE")
                }
                .padding(
                    EdgeInsets(
                        top: 5,
                        leading: 10,
                        bottom: 5,
                        trailing: 10
                    )
                )
            }
            .background(Color.green)
            .clipShape(RoundedRectangle(cornerRadius: 30))
        }
    }
}

struct PlaygroundView_Previews: PreviewProvider {
    static var previews: some View {
        Group() {
            PlaygroundView()
                .previewDisplayName("Default")

            PlaygroundView()
                .previewLayout(PreviewLayout.sizeThatFits)
                .padding()
                .background(Color(.systemBackground))
                .environment(\.colorScheme, .dark)
                .previewDisplayName("Very custom")
        }
    }
}
